# How To Use AirMouse

This guide is for a new user who downloads the project from GitHub and wants to run it locally.

## What AirMouse Does

AirMouse uses your webcam to track your hand and move the mouse cursor.

- Move your index finger to move the cursor
- Pinch thumb + index finger to left click
- Pinch twice quickly to double click
- Press `Esc` to stop the app

## Before You Start

You need:

- A computer with a webcam
- Python 3.11 installed
- Git installed
- A desktop session with permission to control the mouse

## 1. Download The Project

Open Terminal on macOS or PowerShell on Windows.

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPO_URL>
```

Go into the project folder:

```bash
cd <YOUR_REPO_FOLDER>
```

## 2. Create A Virtual Environment

### macOS

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
```

If PowerShell blocks activation, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then close and reopen PowerShell, go back to the project folder, and activate the environment again.

## 3. Install Dependencies

Install the required packages:

```bash
pip install --upgrade pip
pip install -r airmouse/requirements.txt
```

Important:

- This project currently pins `mediapipe==0.10.21`
- Do not upgrade MediaPipe unless the code is updated to the newer Tasks API

## 4. Run The App

From the project root, run:

```bash
python -m airmouse.main
```

If everything is working:

- Your webcam window opens
- You see hand landmarks drawn on the video
- A yellow active box appears
- Moving your index fingertip moves the cursor

## 5. First-Time Permissions

### macOS

You may need to allow:

- `Camera`
- `Accessibility`

Open:

- `System Settings` → `Privacy & Security` → `Camera`
- `System Settings` → `Privacy & Security` → `Accessibility`

Enable permission for your Terminal app or Python interpreter.

### Windows

If needed, allow:

- Camera access for desktop apps

Open:

- `Settings` → `Privacy & security` → `Camera`

Make sure camera access is enabled.

## 6. How To Use It

### Move Cursor

- Hold one hand in front of the webcam
- Keep your hand inside the yellow rectangle
- Move your index fingertip to control the cursor

### Left Click

- Touch your thumb tip and index finger tip together
- Release

### Double Click

- Do two thumb + index pinches quickly

### Right Click

- Touch your thumb tip and middle finger tip together
- Release

### Drag

- Hold the thumb + index pinch for about half a second
- Move your hand while holding
- Release to drop

### Exit

- Press `Esc` in the webcam window
- Or press `Ctrl + C` in Terminal

## 7. How To Run It Again Later

Each time you want to use it again:

### macOS

```bash
cd <YOUR_REPO_FOLDER>
source .venv/bin/activate
python -m airmouse.main
```

### Windows

```powershell
cd <YOUR_REPO_FOLDER>
.venv\Scripts\activate
python -m airmouse.main
```

## 8. How To Stop It

- Press `Esc` while the webcam window is active
- Or press `Ctrl + C` in the terminal window

## 9. Troubleshooting

### Problem: Webcam window does not open

Try:

- Close other apps using the webcam
- Check OS camera permissions
- Restart the app

### Problem: Cursor does not move

Try:

- Make sure your hand landmarks are visible in the webcam window
- On macOS, confirm `Accessibility` permission is enabled
- Keep your hand inside the yellow box

### Problem: Clicks do not work well

Try:

- Improve room lighting
- Keep only one hand visible
- Move slightly farther back from the camera

### Problem: MediaPipe error appears

Run:

```bash
pip uninstall -y mediapipe
pip install mediapipe==0.10.21
```

Then start the app again:

```bash
python -m airmouse.main
```

## 10. Privacy Notes

AirMouse runs locally on your device.

- It uses your webcam while the app is open
- It controls your mouse while the app is running
- It does not upload video to a server
- It does not use cloud APIs

Still, only run software from sources you trust, because camera and accessibility permissions are sensitive.

## 11. Recommended GitHub README Snippet

If you upload this project to GitHub, add a line in your README like this:

```md
For first-time setup and step-by-step instructions, see [HOW_TO_USE.md](./airmouse/HOW_TO_USE.md).
```
