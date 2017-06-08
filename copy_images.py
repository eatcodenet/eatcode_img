import argparse
import logging
import shutil

import eatcode_img.scan_dir


def _init():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", help="source dir of images")
    parser.add_argument("dest_dir", help="destination dir")
    parser.add_argument("filter", help="filter clause")
    parser.add_argument("--log", help="optional log level, default is WARN")
    _args = parser.parse_args()
    if _args.log:
        logging.basicConfig(level=_args.log)
    return _args


def copy_images(src_dir, dest_dir, filter_predicate):
    images = eatcode_img.scan_dir.scan(src_dir)
    filtered = [i for i in images if eval("i." + filter_predicate)]
    for src_img in filtered:
        logging.debug("copying {} to dir {}".format(src_img, dest_dir))
        shutil.copy2(src_img.name, dest_dir)


if __name__ == '__main__':
    args = _init()
    copy_images(args.src_dir, args.dest_dir, args.filter)
