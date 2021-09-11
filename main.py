# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np


def flipColor():
    img = cv2.imread("icons14.png", -1)
    # 特定の色を別の色に置換する
    # 透過部分と色つき部分を反転させる
    # img[:, :, 3] がαチャネルになるので反転させる
    img[:, :, 3] = 255 - img[:, :, 3]
    # img[:, :, 0:2:] = 255
    cv2.imwrite("flip.png", img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flipColor()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
