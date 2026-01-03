"""
Configuration file for the Lane Detection Robot Car
Adjust these settings to match your hardware and track setup
"""
import numpy as np

# ============================================
# Camera Settings
# ============================================
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
CAMERA_FPS = 10  # Frames per second

# ============================================
# Lane Detection Settings
# ============================================
# HSV color range for lane line detection
# Default values work for yellow/orange tape
# Adjust these based on your track's lane line color
LOWER_HSV = np.array([26, 207, 39])
UPPER_HSV = np.array([179, 255, 255])

# Edge detection parameters
CANNY_LOW_THRESHOLD = 200
CANNY_HIGH_THRESHOLD = 400

# Hough transform parameters
HOUGH_RHO = 1  # Distance precision in pixels
HOUGH_THETA = np.pi / 180  # Angular precision in radians (1 degree)
HOUGH_THRESHOLD = 20  # Minimum number of votes
HOUGH_MIN_LINE_LENGTH = 20  # Minimum line length
HOUGH_MAX_LINE_GAP = 14  # Maximum gap between line segments

# Region of interest
ROI_START_HEIGHT = 0.5  # Start from middle of frame (0.0 = top, 1.0 = bottom)

# ============================================
# Motor Settings
# ============================================
DEFAULT_SPEED = 40  # Default motor speed (0-100)

# Motor correction values to compensate for motor differences
# Adjust these if the robot drifts to one side when driving straight
MOTOR_CORRECTION_LEFT = -18
MOTOR_CORRECTION_RIGHT = 0

# ============================================
# Servo Settings
# ============================================
SERVO_CENTER = 90  # Center position for servo (degrees)
SERVO_CHANNEL = '4'  # PCA9685 channel for steering servo

# ============================================
# LED Settings
# ============================================
# Turn signal colors (R, G, B)
TURN_SIGNAL_COLOR = (255, 215, 0)  # Gold/yellow
LED_OFF = (0, 0, 0)

# ============================================
# Web Interface Settings
# ============================================
WEB_HOST = '0.0.0.0'  # Listen on all network interfaces
WEB_PORT = 80  # Default HTTP port (requires sudo)
# Note: If port 80 gives permission errors, change to 5000

# ============================================
# Debug Settings
# ============================================
DEBUG_MODE = False  # Set to True to enable debug logging
SHOW_DETECTION_WINDOWS = False  # Show OpenCV windows (only works with display)
