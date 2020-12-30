# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/30 8:59
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : tesseract.py
# @Software : PyCharm

from PIL import Image
from PIL import ImageEnhance
import pytesseract
import numpy as np
import cv2


def processing_image():
    image_obj = Image.open('./1234.png')  # 获取验证码
    img = image_obj.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    threshold = 160
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    # img.save('./11.png')
    return img


def delete_spot():
    images = processing_image()
    data = images.getdata()
    w, h = images.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    images.putpixel((x, y), 255)
                black_point = 0
    # images.show()
    images.save('./155.png')


def image_str(images):
    image = Image.open(images)
    result = pytesseract.image_to_string(image)  # 图片转文字
    print(result)  # 打印识别的验证码


def ssss():
    imgimgName = './152.png'
    imgName = '1.png'
    # 使用路径导入图片
    im = Image.open(imgimgName)
    # 使用 byte 流导入图片
    # im = Image.open(io.BytesIO(b))
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save('gray-' + imgName)
    # 二值化，采用阈值分割法，threshold为分割点
    threshold = 140
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.save('b' + imgName)


image_str('./153.png')
delete_spot()
