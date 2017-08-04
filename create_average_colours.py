import argparse
import logging

import eatcode_img.average_colour
import eatcode_img.scan_dir


def _init():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", help="source dir of images")
    parser.add_argument("--log", help="optional log level, default is WARN")
    _args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    return _args


def create_averages(src_dir):
    logger = logging.getLogger("eatcode")
    images = eatcode_img.scan_dir.scan(src_dir)
    for img in images:
        logger.info("processing file %s", img.name)
        eatcode_img.average_colour.average(img.name)


if __name__ == '__main__':
    args = _init()
    print(args)
    create_averages(args.src_dir)
