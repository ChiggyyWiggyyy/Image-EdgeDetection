import cv2
import time
import numpy as np
import imutils
from Motor import *
from Servo import *
from CalcAngle import *
import sys
from picamera import PiCamera
from picamera.array import PiRGBArray
from config import *

SCREEN_WIDTH = CAMERA_WIDTH
SCREEN_HEIGHT = CAMERA_HEIGHT
camera = PiCamera()

camera.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
camera.framerate = CAMERA_FPS
rawCapture = PiRGBArray(camera, size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Allow the camera to warmup
time.sleep(0.1)

PWM = Motor()
SRV = Servo()
# Initialize CalcAngle with proper color parameters from config
CLC = CalcAngle(SCREEN_HEIGHT, SCREEN_WIDTH, LOWER_HSV, UPPER_HSV)

def main():
    """
    Main autonomous driving loop.
    Continuously captures frames, detects lanes, and adjusts steering.
    """
    print("Starting autonomous mode...")
    print("Press Ctrl+C to stop")
    
    for frame_data in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Get the frame array
        frame = frame_data.array
        
        # Rotate frame 180 degrees (adjust based on camera mounting)
        frame = imutils.rotate(frame, angle=180)
        
        # Calculate steering angle based on detected lanes
        angle = CLC.get_angle(frame)
        
        # Set servo to calculated angle
        SRV.setServoPwm(SERVO_CHANNEL, angle)
        
        # Move forward with specified speed and motor corrections
        PWM.setMotorModel(DEFAULT_SPEED, DEFAULT_SPEED, MOTOR_CORRECTION_LEFT, MOTOR_CORRECTION_RIGHT)
        
        # Clear the stream for the next frame
        rawCapture.truncate(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        # Clean shutdown
        print("Shutting down motors and servos...")
        PWM.setMotorModel(0, 0, 0, 0)  # Stop all motors
        SRV.setServoPwm(SERVO_CHANNEL, SERVO_CENTER)  # Center the servo
        camera.close()
        print("Bye!")
        sys.exit()