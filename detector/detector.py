import os
from typing import Dict, Any

import boto3


class Detector:
    def __init__(self, region='us-east-2'):
        self.rekognition_client = boto3.client('rekognition', region_name=region)

    # Takes an argument (b64_bytes) which is a stream of bytes which is EITHER a JPEG or PNG formatted
    # file which is a maximum of 5 MB in length (encoded), it also accepts a max_labels, and min_confidence arguments
    # which are defaulted to 5 and 0.75 respectively. This means that Rekognition will not exceed 5 labels and each
    # individual label must be at least 85% confident in its detection of a particular object to be included in the
    # result set.
    def detect_image(self, b64_bytes, max_labels=5, min_confidence=0.75):
        return_result_set: Dict[str, float] = {}
        resp = self.rekognition_client.detect_labels(
            Image={
                'Bytes': b64_bytes,
            },
            MaxLabels=max_labels,
            MinConfidence=min_confidence
        )

        for rslt in resp['Labels']:
            return_result_set[rslt['Name']] = rslt['Confidence']
        return return_result_set