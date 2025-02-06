#!/usr/bin/env python3

from PIL import Image
from argparse import ArgumentParser
import numpy

SAMPLE_WIDTH = 5
SAMPLE_HEIGHT = 5

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--image-path", required=True)
    return parser.parse_args()


def main(image_path):

    img = Image.open(image_path).convert(mode='L')
    img = numpy.array(img)
    print(img.shape, img.dtype)

    Image.fromarray(img).save("test.png")
    # output = numpy.zeros(img.shape[0] / SAMPLE_HEIGHT,  img.shape[1] / SAMPLE_WIDTH)

    for y in range(int(img.shape[0] / SAMPLE_HEIGHT)):
        for x in range(int(img.shape[1] / SAMPLE_WIDTH)):
            y_start = y * SAMPLE_HEIGHT
            y_end = y_start + SAMPLE_HEIGHT
            x_start = x * SAMPLE_WIDTH
            x_end = x_start + SAMPLE_WIDTH
            print(img[y_start:y_end,x_start:x_end])
            break
        break


if __name__ == "__main__":
    main(**vars(parse_args()))
