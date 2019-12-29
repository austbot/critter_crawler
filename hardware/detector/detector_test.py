import unittest
import base64
import detector

class TestDetector(unittest.TestCase):
    def test_detect_image(self):
        """
        Test that it can use the rekognition service and detect labels
        """
        with open("landscape_resized.jpg", "rb") as image_file:
            d = detector.Detector()
            rs = d.detect_image(image_file.read())
            self.assertIn("Building", rs.keys())
            self.assertIn("City", rs.keys())


if __name__ == '__main__':
    unittest.main()
