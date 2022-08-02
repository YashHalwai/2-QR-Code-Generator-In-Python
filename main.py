# Advanced QR code generator in Python

import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1, 
error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=10)

qr.add_data("https://www.linkedin.com/in/yash-halwai-198007203/")

qr.make(fit=True)
img = qr.make_image(fill_color = "blue", back_color = "white")

img.save("Yash_Halwai_LinkedIn.png")