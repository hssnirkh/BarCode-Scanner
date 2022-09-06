#lib
import qrcode 
#create simple .png file from "helo word!"
"""
img = qrcode.make("helo wold!")
img.save("helo.png")
"""

qr = qrcode.QRCode(
version = 1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size = 10,
border = 4,
)
qr.add_data("https://github.com/hssnirkh")
qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="black")
img.save("git3.png")
