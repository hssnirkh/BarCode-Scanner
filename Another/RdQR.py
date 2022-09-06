import qrcode
import cv2
img = cv2.imread("qrcode3.png")
det = cv2.QRCodeDetector()

"""val = det.detectAndDecode(img)
for x in val:
	print(val)"""
val ,pts ,st_code = det.detectAndDecode(img)
print(val)
print(pts)
print(st_code)
print(type(val))

if (val == True):
	print("error")

