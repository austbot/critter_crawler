import time
import RPi.GPIO as gp
import os
import schedule
gp.setwarnings(False)
gp.setmode(gp.BOARD)
from components.camera import Camera
from detector.detector import Detector
PHOTO_TIMEOUT = os.getenv("PHOTO_TIMEOUT", 60)
print("Running Program")
time.sleep(1)
def main():
    print("Running Task")
    camera = Camera()
    d = Detector()
    rs = d.detect_image(camera.capture())
    print(rs)
    for obj, confidence in rs.items():
        print('Object {} : Confidence {}'.format(obj, confidence))

schedule.every(20).seconds.do(main)

while True:
    print("Starting Loop")
    schedule.run_pending()
    time.sleep(1)
