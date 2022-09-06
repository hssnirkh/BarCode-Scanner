import qrcode

data = input("Pls Enter URL:")
fileName = input("pls Enter Name Of Image:")
s = fileName + ".png"
img = qrcode.make(data)

img.save(s)
