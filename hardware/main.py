import time
import RPi.GPIO as gp
import os
import schedule
gp.setwarnings(False)
gp.setmode(gp.BOARD)
from components.camera import Camera
from detector.detector import Detector
PHOTO_TIMEOUT = os.getenv("PHOTO_TIMEOUT", 60)

def main():
    camera = Camera()
    d = Detector()
    rs = d.detect_image(camera.capture())
    for obj, confidence in rs:
        print('Object {} : Confidence {}'.format(obj, confidence))

schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
