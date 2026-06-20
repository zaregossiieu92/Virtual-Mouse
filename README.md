# AirMouse

AirMouse is a local-first desktop MVP that turns a laptop webcam into a hand-gesture mouse controller. It tracks one hand with MediaPipe, maps the index fingertip to the full screen, smooths cursor motion, and converts pinch gestures into mouse actions.

## Features

- Real-time single-hand tracking with MediaPipe Hands
- Cursor control using the index fingertip
- Inner active-region mapping to improve edge control
- Exponential smoothing for landmarks and cursor movement
- Single click with thumb + index pinch
- Double click with two pinches inside a configurable time window
- Optional right click with thumb + middle finger pinch
- Optional drag by holding a pinch
- Live webcam preview with landmarks, active region, FPS, and gesture status
- Emergency exit with `Esc`

## Project Structure

```text
airmouse/
├── README.md
├── requirements.txt
├── __init__.py
├── config.py
├── main.py
├── hand_tracking/
│   ├── __init__.py
│   ├── detector.py
│   └── gestures.py
├── mouse/
│   ├── __init__.py
│   ├── controller.py
│   └── mapper.py
├── ui/
│   ├── __init__.py
│   └── overlay.py
├── utils/
│   ├── __init__.py
│   ├── fps.py
│   ├── smoothing.py
│   └── state_machine.py
└── tests/
    ├── __init__.py
    ├── test_gestures.py
    ├── test_mapper.py
    └── test_state_machine.py
```

## Requirements

- Python 3.11+
- Webcam
- Desktop accessibility permission for mouse control
- Desktop display server that supports `pyautogui`

## Installation

1. Create and activate a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r airmouse/requirements.txt
```

AirMouse currently targets the legacy MediaPipe Hands API, so `mediapipe==0.10.21` is pinned intentionally for compatibility.

## Run

Start the app from the project root:

```bash
python -m airmouse.main
```

If you prefer, you can also run:

```bash
python airmouse/main.py
```

## Testing

Run the automated tests from the project root:

```bash
pytest airmouse/tests
```

## Gesture Guide

- Move cursor: point with your index fingertip inside the yellow active box
- Left click: pinch thumb + index finger and release
- Double click: perform two thumb + index pinches within `350ms`
- Right click: pinch thumb + middle finger and release
- Drag: hold a thumb + index pinch for at least `500ms`, then release to drop
- Exit: press `Esc`

## Calibration Tips

- Keep your hand inside the yellow active region for the most predictable mapping
- Sit far enough back that the full hand stays visible
- Use stable lighting to reduce landmark jitter
- If cursor motion feels too floaty, increase `SMOOTHING_ALPHA`
- If clicks misfire, increase `PINCH_THRESHOLD` slightly or reduce background clutter

## Configuration

Tune values in [config.py](/Users/gauravkumar/Documents/New%20project%202/airmouse/config.py):

- `PINCH_THRESHOLD`
- `RIGHT_CLICK_THRESHOLD`
- `DOUBLE_CLICK_WINDOW`
- `SMOOTHING_ALPHA`
- `LANDMARK_SMOOTHING_ALPHA`
- `ACTIVE_REGION_MARGIN`
- `CLICK_COOLDOWN`
- `DRAG_HOLD_TIME`

## Troubleshooting

### Webcam does not open

- Confirm no other app is using the camera
- Grant camera permission to your terminal or Python app
- Try a different `CAMERA_INDEX` in `config.py`

### Cursor does not move

- On macOS, grant Accessibility permission to the terminal or Python interpreter
- On Linux, ensure you are running inside a graphical desktop session
- Verify the hand landmarks are visible in the preview window

### Clicks feel delayed

- This is expected for single clicks because AirMouse waits briefly to determine whether a double click is intended
- Reduce `DOUBLE_CLICK_WINDOW` if you prefer faster single-click confirmation

### MediaPipe install issues

- Upgrade pip first: `python -m pip install --upgrade pip`
- If you already installed a newer MediaPipe such as `0.10.31+`, reinstall the pinned version:

```bash
pip uninstall -y mediapipe
pip install mediapipe==0.10.21
```

- On Apple Silicon, use a current Python 3.11 build
- If a platform-specific wheel is unavailable, try recreating the environment with a newer pip version

## Screenshots

Placeholder for future screenshots of:

- Webcam preview with landmarks
- Active region overlay
- Gesture status display

## Future Improvements

- Dedicated settings UI for thresholds and smoothing
- Multi-monitor awareness
- Pause mode gesture
- Gesture-based scrolling
- Personalized calibration workflow
- Better drag heuristics and dwell-click accessibility modes

## Notes

- All processing runs locally
- No cloud APIs are used
- Cursor updates stop when hand tracking is lost
