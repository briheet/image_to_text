#!/usr/bin/env python3

from PIL import Image
from argparse import ArgumentParser
import numpy


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--image-path", required=True)
    return parser.parse_args()


def main(image_path):
    img = Image.open(image_path)
    img = numpy.array(img)
    print(img)

    pass


if __name__ == "__main__":
    main(**vars(parse_args()))
