#!/usr/bin/env python3

import os
import sys
from PIL import Image

# listing all the images variables
# imagesDir = '~/supplier-data/images' # linux
imagesDir = 'supplier-data/images' # windows
imagePath = os.path.expanduser(imagesDir)
images = os.listdir(imagePath)
sourceFormat = "tiff"
distFormat = "jpeg"


for fp in images:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".tiff":
        print (fp, "is an tiff that we will change!")
    elif ext == ".jpeg":
        print (fp, "is a jpeg that we already changed!")
    else:
        print (fp, "is an unknown file format.")


# TODO: You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
"""
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
"""


# TODO: After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.