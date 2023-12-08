import cv2
from Motor import*
from Servo import*
from CalcAngle import*
import sys
from picamera import PiCamera
from picamera.array import PiRGBArray

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
camera = PiCamera()

camera.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
#allow the camera to warmup
time.sleep()

#camera = cv2.VideoCapture(-1)
#camera.set(3, SCREEN_WIDTH)
#camera.set(4, SCREEN_HEIGHT)

PWM = Motor()
SRV = Servo()
CLC = CalcAngle(SCREEN_HEIGHT, SCREEN_WIDTH)

def main():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
        frame = frame.array
        frame = imutils.rotate(frame, angle=180) 
        angle = CLC.get_angle(frame)
        SRV.setServoPwm('4',angle)
        PWM.setMotorModel(40, 40, )
    pass
    """
    while we get a frame 
    compute the angle 
    set the servo 
    set the motor
    """
    
    try:
        main() # run the main function
    except KeyboardInterrupt:
        print("Bye")
    finally:
        PWM.setMotorModel(0,0)
        SRV.setServoPwm('4',)
        camera.close()
        sys.exit()