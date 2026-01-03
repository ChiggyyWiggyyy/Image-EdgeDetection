# 🚗 Lane Detection & Autonomous Robot Car

Welcome! This project is an autonomous lane-following robot car powered by a Raspberry Pi and computer vision. The robot can "see" lane lines using a camera and navigate autonomously by detecting edges and calculating the best steering angle in real-time.

Whether you're a hobbyist, student, or just curious about robotics and computer vision, this guide will help you understand how everything works!

---

## 🎯 What Does This Project Do?

Imagine a small robot car with a camera mounted on it. As it moves forward, the camera captures video of the road ahead. The robot then:

1. **Sees the lane lines** using color detection
2. **Identifies edges** in the image to find where the lines are
3. **Calculates the steering angle** needed to stay centered between the lines
4. **Adjusts its steering** automatically to follow the path

Plus, you can control the robot remotely through a web browser interface with live video streaming!

---

## ✨ Key Features

- 🎥 **Real-time lane detection** using computer vision (OpenCV)
- 🧠 **Automated steering** based on detected lane positions
- 🌐 **Web-based control panel** - drive the robot from your phone or computer
- 📹 **Live video streaming** - see what the robot sees
- 💡 **LED indicators** for turn signals
- 🔊 **Buzzer alerts** when reversing
- 📸 **Image capture** feature for debugging
- ⚡ **Battery monitoring** to track power levels

---

## 🛠️ What You'll Need

### Hardware Components

- **Raspberry Pi** (3 or 4 recommended) - the "brain" of the robot
- **Pi Camera Module** - so the robot can see
- **Robot car chassis** with 4 DC motors - for movement
- **Motor driver board (PCA9685)** - to control the motors
- **Servo motor** - for steering
- **RGB LED strip** - for turn signals
- **Buzzer** - for audio feedback
- **Battery pack** - to power everything
- **SD card** (16GB+) with Raspberry Pi OS installed

### Software Requirements

- Python 3.7 or higher
- OpenCV for image processing
- Flask for the web interface
- Various Python libraries (see `requirements.txt`)

---

## 📦 Installation Guide

### Step 1: Clone the Repository

On your Raspberry Pi, open a terminal and run:

```bash
git clone https://github.com/ChiggyyWiggyyy/Image-EdgeDetection.git
cd Image-EdgeDetection
```

### Step 2: Install Dependencies

Install all the required Python packages:

```bash
pip3 install -r requirements.txt
```

**Note:** Some packages like `RPi.GPIO` and `picamera` only work on Raspberry Pi hardware.

### Step 3: Enable Camera

Make sure the Pi Camera is enabled:

```bash
sudo raspi-config
```

Navigate to `Interface Options` → `Camera` → `Enable`

### Step 4: Configure Your Track

Open `config.py` and adjust the HSV color values to match your track's lane line color. The default values work for yellow/orange tape:

```python
LOWER_HSV = (26, 207, 39)  # Adjust these for your track color
UPPER_HSV = (179, 255, 255)
```

---

## 🚀 How to Run

### Web Control Mode (Recommended for Testing)

Run the Flask web server:

```bash
sudo python3 app.py
```

**Why sudo?** Port 80 requires administrator privileges.

Then, open a web browser and go to:
```
http://<your-raspberry-pi-ip-address>
```

You'll see a control panel where you can:
- View live camera feed
- Control the robot manually (forward, back, turn)
- Capture images
- Monitor battery voltage

### Autonomous Mode

For fully autonomous lane following:

```bash
python3 main.py
```

The robot will start following the lane lines automatically. Press `Ctrl+C` to stop.

---

## 🧪 How It Works (The Technical Magic Explained Simply)

Here's what happens every time the camera captures a frame:

### 1. **Color Filtering**
The image is converted from RGB to HSV (Hue, Saturation, Value) color space. This makes it easier to detect specific colors (like the blue or yellow lane lines) regardless of lighting conditions.

### 2. **Edge Detection**
We use the **Canny edge detection algorithm** to find edges in the filtered image. Edges appear where there's a sharp change in color or brightness - perfect for detecting lane lines!

### 3. **Region of Interest**
We only look at the bottom half of the image (where the road is) and ignore the top half (sky, background). This makes processing faster and more accurate.

### 4. **Line Detection**
The **Hough Transform** algorithm finds straight lines in the edge-detected image. It identifies all the line segments that could be lane markings.

### 5. **Line Averaging**
Multiple detected line segments are averaged together to create two main lines: left lane and right lane. The algorithm separates them based on their slope (negative slope = left lane, positive slope = right lane).

### 6. **Steering Angle Calculation**
Using the position of the detected lane lines, we calculate how far the robot needs to turn to stay centered. This angle is sent to the servo motor.

### 7. **Motor Control**
The servo adjusts the steering angle, and the DC motors maintain forward speed. The robot continuously adjusts its path to follow the lanes!

---

## 📁 Project Structure

```
Image-EdgeDetection/
├── README.md                   # You are here!
├── requirements.txt            # Python dependencies
├── config.py                   # Configuration settings
├── .gitignore                  # Files to ignore in git
│
├── app.py                      # Flask web server (web control mode)
├── main.py                     # Autonomous driving mode
│
├── CalcAngle.py               # Lane detection and angle calculation
├── camera_opencv.py           # Camera interface
├── base_camera.py             # Base camera class
│
├── Motor.py                   # Motor control
├── Servo.py                   # Servo control
├── Led.py                     # LED control
├── Buzzer.py                  # Buzzer control
├── ADC.py                     # Analog-to-digital converter (battery)
├── PCA9685.py                 # PWM driver chip interface
│
└── edge_detection_demo.ipynb  # Jupyter notebook demo
```

---

## 🎨 Customization Tips

### Adjusting for Different Track Colors

If your lane lines are a different color:

1. Run the `edge_detection_demo.ipynb` notebook
2. Experiment with HSV values until you can clearly detect your lanes
3. Update the values in `config.py`

### Tuning Detection Parameters

In `CalcAngle.py`, you can adjust:

- **Canny thresholds** (`200, 400`) - higher = fewer edges detected
- **Hough parameters** - adjust sensitivity of line detection
- **Region of interest** - change which part of image to analyze
- **Speed settings** - in `config.py`, adjust `DEFAULT_SPEED`

### Motor Correction

If the robot drifts to one side when driving straight, adjust the correction values in `config.py`:

```python
MOTOR_CORRECTION_LEFT = -18   # Adjust these to compensate
MOTOR_CORRECTION_RIGHT = 0    # for motor differences
```

---

## 🐛 Troubleshooting

### Camera Not Working

- Make sure the camera is enabled: `sudo raspi-config`
- Check the ribbon cable connection
- Test with: `raspistill -o test.jpg`

### Robot Not Detecting Lanes

- Check your HSV color values match your track
- Ensure good lighting conditions
- Make sure lane lines are clearly visible and contrasting with the background

### Web Interface Not Loading

- Verify the Flask server is running: `sudo python3 app.py`
- Check your Raspberry Pi's IP address: `hostname -I`
- Make sure you're on the same network
- Try port 5000 if port 80 doesn't work: modify `WEB_PORT` in `config.py`

### Permission Errors

- GPIO operations need sudo: `sudo python3 app.py`
- Add your user to gpio group: `sudo usermod -a -G gpio $USER`

---

## 🧑‍💻 For Developers

### Running Tests

```bash
python3 -m pytest tests/
```

### Code Structure

- **Hardware abstraction**: All hardware components are in separate modules for easy testing
- **Vision processing**: `CalcAngle.py` contains all computer vision logic
- **Web interface**: Flask app in `app.py` with REST API endpoints
- **Configuration**: Centralized in `config.py` for easy adjustments

### Contributing

Contributions are welcome! Feel free to:
- Report bugs by opening an issue
- Suggest improvements
- Submit pull requests

---

## 📚 Learn More

Want to dive deeper into the concepts?

- **Computer Vision**: [OpenCV Documentation](https://docs.opencv.org/)
- **Edge Detection**: Learn about Canny edge detection and Hough transforms
- **Raspberry Pi GPIO**: [Official GPIO documentation](https://www.raspberrypi.org/documentation/usage/gpio/)
- **Flask Framework**: [Flask quickstart guide](https://flask.palletsprojects.com/)

---

## 📝 Project Background

This project demonstrates practical applications of:
- Computer vision and image processing
- Real-time embedded systems
- Autonomous navigation algorithms
- Web-based IoT interfaces
- Hardware-software integration

It's great for learning about robotics, computer vision, and embedded systems programming!

---

## 🙏 Acknowledgments

Built with:
- **OpenCV** - Computer vision library
- **Flask** - Web framework
- **NumPy** - Numerical computing
- **Raspberry Pi** - Amazing single-board computer

---

## 📧 Questions?

If you have questions or run into issues, feel free to:
- Open an issue on GitHub
- Check existing issues for solutions
- Experiment and learn - that's what robotics is all about!

---

## ⚖️ License

This project is open source and available under the MIT License.

---

**Happy building! 🚗💨**

Remember: Every expert was once a beginner. Don't worry if things don't work perfectly the first time - debugging and iteration are part of the learning process!
