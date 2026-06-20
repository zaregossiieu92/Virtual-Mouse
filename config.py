"""Application configuration for AirMouse."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

PINCH_THRESHOLD = 0.04
RIGHT_CLICK_THRESHOLD = 0.045
DOUBLE_CLICK_WINDOW = 0.35
SMOOTHING_ALPHA = 0.25
LANDMARK_SMOOTHING_ALPHA = 0.35
ACTIVE_REGION_MARGIN = 0.10
CLICK_COOLDOWN = 0.15
DRAG_HOLD_TIME = 0.50
CAMERA_INDEX = 0
FRAME_WIDTH = 960
FRAME_HEIGHT = 540
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7
MAX_NUM_HANDS = 1
WINDOW_NAME = "AirMouse"
SHOW_PREVIEW = True


@dataclass(frozen=True)
class AppConfig:
    """Container for tunable application settings."""

    pinch_threshold: float = PINCH_THRESHOLD
    right_click_threshold: float = RIGHT_CLICK_THRESHOLD
    double_click_window: float = DOUBLE_CLICK_WINDOW
    smoothing_alpha: float = SMOOTHING_ALPHA
    landmark_smoothing_alpha: float = LANDMARK_SMOOTHING_ALPHA
    active_region_margin: float = ACTIVE_REGION_MARGIN
    click_cooldown: float = CLICK_COOLDOWN
    drag_hold_time: float = DRAG_HOLD_TIME
    camera_index: int = CAMERA_INDEX
    frame_width: int = FRAME_WIDTH
    frame_height: int = FRAME_HEIGHT
    min_detection_confidence: float = MIN_DETECTION_CONFIDENCE
    min_tracking_confidence: float = MIN_TRACKING_CONFIDENCE
    max_num_hands: int = MAX_NUM_HANDS
    window_name: str = WINDOW_NAME
    show_preview: bool = SHOW_PREVIEW

    @property
    def project_root(self) -> Path:
        return Path(__file__).resolve().parent

