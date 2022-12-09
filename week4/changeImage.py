#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image


def convert_images(self):
    new_image = Image.open(imagePath + '/' + fp)
    new_image.convert('RGB').resize((600, 400)).save(imagePath + '/' + fp[:-5] + '.jpeg')
    print(new_image, " is converted")


if __name__ == '__main__':
    #imagesDir = '~/supplier-data/images'  # linux
    imagesDir = 'supplier-data/images'  # windows
    imagePath = os.path.expanduser(imagesDir)
    images = os.listdir(imagePath)
    sourceFormat = "tiff"
    distFormat = "jpeg"

    for fp in images:

        if Path(fp).suffix == '.tiff':
            print(fp, "is an tiff that we will change!")
            convert_images(fp)

        elif Path(fp).suffix == '.jpeg':
            print(fp, "is a jpeg that we already changed!")

        else:
            print(fp, "is an unknown file format.")
