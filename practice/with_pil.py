# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open("source/img/fox.jpg")
width, height = im.size
print (width, height)
