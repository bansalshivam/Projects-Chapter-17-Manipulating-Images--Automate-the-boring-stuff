"""Identifying Photo Folders on the Hard Drive"""

import os
from PIL import Image

image_size = 500

for foldername, subfolders, filenames in os.walk('/home'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not(filename.lower().endswith(('.png', '.jpg', '.gif'))):
            numNonPhotoFiles += 1
            continue
        try:
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue

        width, height = im.size

        if width > image_size and height > image_size:
            numPhotoFiles += 1

        else:
            numNonPhotoFiles += 1

    print('\nFolder - ' + foldername)
    print('Photo - ' + str(numPhotoFiles))
    print('Non Photo - ' + str(numNonPhotoFiles))

    # if numPhotoFiles > numNonPhotoFiles:
    #     print(os.path.abspath(foldername))
