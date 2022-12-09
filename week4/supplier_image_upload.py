#!/usr/bin/env python3


import requests
import os
from pathlib import Path

url = "http://localhost/upload/"
source_images = '~/supplier-data/images'
Source_path = os.path.expanduser(source_images)
images = os.listdir(Source_path)

for image in images:
    if Path(image).suffix == '.jpeg':
        with open(Source_path + '/' + image, 'rb') as opened:
            print("Uploading file : " + image)
            r = requests.post(url, files={'file': opened})
