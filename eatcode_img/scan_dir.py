import os
import subprocess

import eatcode_img


def scan_dir(img_dir):
    _images = []
    for entry in os.scandir(img_dir):
        cmd = ["identify", "-format", "%m,%h,%w,%M", (img_dir + os.sep + entry.name)]
        output = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("UTF-8").strip()
        (img_type, img_height, img_width, img_name) = output.split(",")
        _images.append(eatcode_img.Image(img_name, img_height, img_width, img_type))
    return _images


if __name__ == '__main__':
    images = scan_dir('/home/ayub/Pictures')
    for img in images:
        print(img)
