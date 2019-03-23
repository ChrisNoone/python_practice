# -*- coding: utf-8 -*-

import base64

image = "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"
fh = open("source/img/with_base64.jpg", "wb")
fh.write(base64.b64decode(image))
fh.close()


# with open("source/img/fox.jpg", "rb") as imageFile:
#     str = base64.b64encode(imageFile.read())
#     print (str)