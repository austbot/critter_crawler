import time
from io import BytesIO
from picamera import PiCamera

class Camera:
    def __init__(self):
        self._ledState = 0
        self.cam = PiCamera()
        self.cam.resolution = (320, 240)

    def ledState(self, num):
        self._ledState = num

    def capture(self):
        my_stream = BytesIO()
        self.led.setState(self.ledState)
        self.camera.capture(my_stream, 'jpeg')
        return my_stream


__all__ = [
    "Camera"
]
