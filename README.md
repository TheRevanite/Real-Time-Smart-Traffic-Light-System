
# Smart Traffic Signal Controller using Raspberry Pi

This project is designed to automate traffic signal timing based on live image processing. It utilizes a Raspberry Pi, Pi Camera 2, and GPIO components to dynamically adjust the green light duration according to traffic conditions.

## 🛠️ Project Structure

| File | Description |
|------|-------------|
| `camera_capture.py` | Captures an image using the Pi Camera 2. |
| `image_processing.py` | Processes the captured image using Canny Edge Detection to assess traffic density. |
| `lights.py` | Sets the duration of the green signal based on processed image data. |
| `lightspigpio.py` | Interfaces with GPIO pins using the `gpiozero` library to control the signal lights. |
| `main.py` | Main script that orchestrates the full process from image capture to signal control. |
| `references.py` | Captures and stores a reference image for background subtraction or comparison. |
| `servomotor.py` | Controls a servo motor to rotate or move at specific time intervals. |
| `__pycache__/` | Contains Python bytecode files (auto-generated). |

## ⚙️ How It Works

1. **Image Capture**: `camera_capture.py` triggers the Pi Camera to capture a real-time image of the traffic lane.
2. **Image Analysis**: `image_processing.py` applies Canny Edge Detection to identify vehicles and estimate traffic density.
3. **Signal Timing**: Based on the density, `lights.py` adjusts the green light duration dynamically.
4. **Signal Control**: `lightspigpio.py` handles GPIO interactions to turn the traffic lights on or off.
5. **Reference Image**: `references.py` allows capturing a reference image to help in differential analysis.
6. **Servo Control**: `servomotor.py` manages timed servo operations (e.g., gate opening/closing).

## 📦 Requirements

- Raspberry Pi 5 (or any model with GPIO support)
- Pi Camera 2
- Traffic Light Modules
- Servo Motor
- Python 3.x
- Libraries:
  - `gpiozero`
  - `opencv-python`
  - `numpy`

Install Python dependencies:

```bash
pip install gpiozero opencv-python numpy
```

## 🚀 Getting Started

1. Connect your Pi Camera and traffic signal LEDs to GPIO pins.
2. Run the main script:

```bash
python main.py
```

3. The system will:
   - Capture an image.
   - Analyze traffic density.
   - Adjust green signal timing.
   - Rotate servo motor (if applicable).

## 🧠 Future Improvements

- Integrate with cloud for data logging.
- Add GUI to visualize traffic and timings.
- Expand to multi-lane or multi-signal support.

## ⚠️ Disclaimer

Ensure safe practices when working with electronics and live environments. Use dummy loads during development.

---
