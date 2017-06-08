import os
import subprocess

import eatcode_img


def scan(img_dir):
    _images = []
    for entry in os.scandir(img_dir):
        cmd = ["identify", "-format", "%h,%w,%b,%m,%M", (img_dir + os.sep + entry.name)]
        output = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("UTF-8").strip()
        (_height, _width, _size_bytes, _image_format, _name) = output.split(",")
        _images.append(eatcode_img.Image(_name, int(_height), int(_width), int(_size_bytes[:-1]), _image_format))
    return _images
