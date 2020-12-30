# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/30 8:59
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : tesseract.py
# @Software : PyCharm

from PIL import Image
from PIL import ImageEnhance
import pytesseract

img = Image.open('153.png')
img = img.convert('RGB')  # 这里也可以尝试使用L
enhancer = ImageEnhance.Color(img)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
img = enhancer.enhance(20)
img.show(img)
text = pytesseract.image_to_string(img)
print(text)


image = Image.open(r'./153.png')

text1 = pytesseract.image_to_string(image)
print(text1)

