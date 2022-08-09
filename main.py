"""
****** IMPORTANT *******
This example will run on Python3.8 and OpenCV4.


There are some assumptions:
  1. The input is the result of yolo sign detection (ex. data/images/panel.jpg)
  2. The top left bit is always on
  3. The resolution is high enough
  4. The image size is 640x320
  5. There is no rotation in image
  6. There is no prespective in image
  7. All panels are the same size (64x32)


Usage:
    python3 main.py --source path/to/image
    
    Example:
        python3 main.py --source data/images/image.jpg

    or use default path:
        python3 main.py

"""

import argparse
import os
import sys
from pathlib import Path

from utils.contour import bit_detecttion


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default=ROOT / 'data/images/panel.jpg', help='file/dir/URL/glob')
    opt = parser.parse_args()
    return opt


def main(opt):
    bit_detecttion(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
