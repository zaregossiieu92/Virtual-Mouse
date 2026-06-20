"""Entry point for the AirMouse desktop MVP."""

from __future__ import annotations

import sys
import time
from pathlib import Path

import cv2

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from airmouse.config import AppConfig
from airmouse.hand_tracking.detector import HandDetector
from airmouse.hand_tracking.gestures import GestureEvent, GestureRecognizer
from airmouse.mouse.controller import MouseController
from airmouse.mouse.mapper import CoordinateMapper, ScreenBounds
from airmouse.ui.overlay import OverlayRenderer
from airmouse.utils.fps import FPSCounter
from airmouse.utils.smoothing import ExponentialSmoother


def main() -> int:
    config = AppConfig()
    mouse = MouseController()
    screen_width, screen_height = mouse.screen_size()
    mapper = CoordinateMapper(
        screen_bounds=ScreenBounds(width=screen_width, height=screen_height),
        active_region_margin=config.active_region_margin,
    )
    cursor_smoother = ExponentialSmoother(alpha=config.smoothing_alpha)
    detector = HandDetector(config)
    gestures = GestureRecognizer(config)
    overlay = OverlayRenderer()
    fps_counter = FPSCounter()

    capture = cv2.VideoCapture(config.camera_index)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, config.frame_width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, config.frame_height)

    if not capture.isOpened():
        print("Unable to open the webcam. Check camera permissions and device availability.")
        detector.close()
        return 1

    cursor_position: tuple[int, int] | None = None
    gesture_snapshot = gestures.update(None, time.perf_counter())

    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                print("Failed to read a frame from the webcam.")
                break

            frame = cv2.flip(frame, 1)
            observation, results = detector.process(frame)
            now = time.perf_counter()
            gesture_snapshot = gestures.update(observation, now)

            if observation is not None:
                mapped_x, mapped_y = mapper.map_point(observation.index_tip)
                smooth_x, smooth_y = cursor_smoother.update((mapped_x, mapped_y))
                cursor_position = (int(smooth_x), int(smooth_y))
                mouse.move(*cursor_position)
            else:
                cursor_smoother.reset()

            _apply_mouse_actions(mouse, gesture_snapshot.gesture)

            fps = fps_counter.tick()
            if config.show_preview:
                preview = overlay.draw(
                    frame=frame,
                    observation=observation,
                    mediapipe_results=results,
                    gesture=gesture_snapshot,
                    fps=fps,
                    tracking_active=observation is not None,
                    active_region_margin=config.active_region_margin,
                    cursor_position=cursor_position,
                )
                cv2.imshow(config.window_name, preview)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break
    finally:
        if gesture_snapshot.is_dragging:
            mouse.mouse_up()
        capture.release()
        detector.close()
        if config.show_preview:
            cv2.destroyAllWindows()

    return 0


def _apply_mouse_actions(mouse: MouseController, gesture: GestureEvent) -> None:
    if gesture is GestureEvent.PINCH:
        mouse.click()
    elif gesture is GestureEvent.DOUBLE_PINCH:
        mouse.double_click()
    elif gesture is GestureEvent.RIGHT_CLICK:
        mouse.right_click()
    elif gesture is GestureEvent.DRAG_START:
        mouse.mouse_down()
    elif gesture is GestureEvent.DRAG_END:
        mouse.mouse_up()


if __name__ == "__main__":
    raise SystemExit(main())
