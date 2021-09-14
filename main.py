# -*- coding: utf-8 -*-
import csv
import json
import cv2
import base64

# 2014 Material Design color palettesにある、
# Red 300, Purple 300, Blue 300, Green 300, Yellow 300, Orange 300, Brown 300, Gray 300の8種類
ICON_COLORS = [{"colorName": "Red", "bgr": [115, 115, 229]},
               {"colorName": "Purple", "bgr": [200, 104, 186]},
               {"colorName": "Blue", "bgr": [246, 181, 100]},
               {"colorName": "Green", "bgr": [132, 199, 129]},
               {"colorName": "Yellow", "bgr": [118, 241, 255]},
               {"colorName": "Orange", "bgr": [77, 183, 255], },
               {"colorName": "Brown", "bgr": [127, 136, 161]},
               {"colorName": "Gray", "bgr": [224, 224, 224]}]

FILE_PREFIX = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]


def makeIcons():
    iconsInfo = []
    for i in FILE_PREFIX:
        iconType = i
        fileName = "icons" + iconType + ".png"
        for n in ICON_COLORS:
            iconInfo = {}
            img = cv2.imread(fileName, -1)
            # 色変え
            img[:, :, 0] = n.get("bgr")[0]
            img[:, :, 1] = n.get("bgr")[1]
            img[:, :, 2] = n.get("bgr")[2]
            # pngで出力したいときは以下のコメントを外す
            cv2.imwrite(n.get("colorName") + "_" + str(i) + "_" + str(n) + ".png", img)
            img_base64 = pil_to_base64(img)
            img_base64Str = img_base64.decode('utf-8')
            iconInfo['iconType'] = iconType
            iconInfo['colorName'] = n.get("colorName")
            iconInfo['base64'] = str(img_base64Str)
            iconsInfo.append(iconInfo)

            # 透過部分と色つき部分を反転させる
            # img[:, :, 3] がαチャネルになるので反転させる
            img[:, :, 3] = 255 - img[:, :, 3]
            # pngで出力したいときは以下のコメントを外す
            cv2.imwrite(n.get("colorName") + "_flip" + str(i) + "_" + str(n) + ".png", img)
            img_base64 = pil_to_base64(img)
            img_base64Str = img_base64.decode('utf-8')
            iconInfo['iconType'] = iconType
            iconInfo['colorName'] = n.get("colorName")
            iconInfo['base64'] = str(img_base64Str)
            iconsInfo.append(iconInfo)
    write_to_json("icons_base64.json", iconsInfo)


def pil_to_base64(img):
    result, dst_data = cv2.imencode('.png', img)
    dst_base64 = base64.b64encode(dst_data)

    return dst_base64

    return b64_data


def write_to_json(fileName, data):
    # 辞書オブジェクトをJSONファイルへ出力
    with open(fileName, mode='wt', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makeIcons()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
