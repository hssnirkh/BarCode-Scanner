import qrcode
import cv2
import numpy as np

file = input("pls enter name of image: ")
fileName = file + ".png"
#data to encode
data = input("pls enter the value you want: ")

#nemone kardan be onvane sheie
#instantiate QRCode Object
qr = qrcode.QRCode(
version = 1,
box_size = 10,
border = 4,
)
#add data to qrcode
qr.add_data(data)

#compile the data in QR code Array
qr.make()

#print the image shape
print("the shape of QR code:",np.array(qr.get_matrix()).shape)

#transfer the array into actual image
img = qr.make_image(fill_color="white",back_color="black")

#save it to file
img.save(fileName)

