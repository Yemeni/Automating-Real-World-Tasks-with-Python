#!/usr/bin/env python3

from PIL import Image
import os

path = "images"
destination = "dest"
list_of_images = os.listdir(path)

target_specs = {
    "degree": -90,
    "dimensions": (128, 128),
    "color": "RGB",
    "format": "jpeg"
}


for file in list_of_images:
    try:
        print("Trying: " + file)
        with Image.open(path + "/" + file) as i:
            print("Opened: " + str(i))
            i = Image.open(path + "/" + file)
            i = i.rotate(target_specs["degree"])
            i = i.resize(target_specs["dimensions"])
            i = i.convert(target_specs["color"])
            i.save(destination + '/' + file, format=target_specs["format"])
            print("Saved")
            i.close()
    except IOError as e:
        print(e)




