# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
import base64
import numpy as np
from PIL import Image

ICONS_BASE64 = []

COLOR = [255, 0, 0]


def flipColor():
    img = cv2.imread("icons13.png", -1)
    # 色変え
    img[:, :, 0] = 255
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    cv2.imwrite("colorChange.png", img)
    img_base64 = pil_to_base64(img)
    img_base64Str = img_base64.decode('utf-8')
    ICONS_BASE64.append(img_base64Str)

    # 透過部分と色つき部分を反転させる
    # img[:, :, 3] がαチャネルになるので反転させる
    img[:, :, 3] = 255 - img[:, :, 3]
    cv2.imwrite("flip.png", img)
    img_base64 = pil_to_base64(img)
    img_base64Str = img_base64.decode('utf-8')
    ICONS_BASE64.append(img_base64Str)
    print(ICONS_BASE64)


def pil_to_base64(img):
    result, dst_data = cv2.imencode('.png', img)
    dst_base64 = base64.b64encode(dst_data)

    return dst_base64

    return b64_data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flipColor()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
