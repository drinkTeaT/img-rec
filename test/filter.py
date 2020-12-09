"""
@file filter2D.py
@brief Sample code that shows how to implement your own linear filters by using filter2D function
"""
import sys
import cv2 as cv
import numpy as np


def main(argv):
    window_name = 'filter2D Demo'

    imageName = argv[0] if len(argv) > 0 else 'img/1.jpg'
    # Loads an image
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1

    ddepth = -1

    ind = 0
    while True:

        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)

        dst = cv.filter2D(src, ddepth, kernel)

        cv.imshow(window_name, dst)
        c = cv.waitKey(500)
        if c == 27:
            break
        ind += 1
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
