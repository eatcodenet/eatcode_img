import argparse
import logging
import shutil
import random
import os
import eatcode_img.scan_dir


def _init():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", help="source dir of images")
    parser.add_argument("dest_dir", help="destination dir")
    parser.add_argument("filter", help="filter clause")
    parser.add_argument("--log", help="optional log level, default is WARN")
    parser.add_argument("--randomise", help="randomise file names on save",
                        action="store_true")
    _args = parser.parse_args()
    if _args.log:
        logging.basicConfig(level=_args.log)
    return _args


def copy_images(src_dir, dst_dir, filter_predicate, randomise=False):
    images = eatcode_img.scan_dir.scan(src_dir)
    filtered = [i for i in images if eval("i." + filter_predicate)]
    randoms = random.sample(["{:04d}".format(x) for x in range(len(filtered))],
                            len(filtered))
    for img in filtered:
        if randomise:
            dst = dst_dir + os.sep + randoms.pop() + "." + img.format.lower()
        else:
            dst = dst_dir
        logging.debug("copying {} to {}".format(img, dst))
        shutil.copy2(img.name, dst)


if __name__ == '__main__':
    args = _init()
    print(args)
    copy_images(args.src_dir, args.dest_dir, args.filter, args.randomise)
