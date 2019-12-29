# Detector

## How to use:

```python
import detector

d = detector.Detector()
with open("landscape_resized.jpg", "rb") as image_file:
    rs = d.detect_image(image_file.read())

for obj, confidence in rs:
    print('Object {} : Confidence {}'.format(obj, confidence))
```