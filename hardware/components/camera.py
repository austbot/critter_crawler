from io import BytesIO
import time
from picamera import PiCamera

class Camera:
    def __init__(self):
        self._ledState = 0
        self.cam = PiCamera()
        self.cam.resolution = (320, 240)
        self.cam.start_preview()
        time.sleep(1)


    def ledState(self, num):
        self._ledState = num

    def capture(self):
        my_stream = BytesIO()
        self.cam.capture(my_stream, format='jpeg')
        return my_stream.getvalue()


__all__ = [
    "Camera"
]
