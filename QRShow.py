import pyqrcode
from pyqrcode import QRCode

Dest = "https://github.com/hssnirkh"

MyQR = QRCode(Dest,error='H',version=None,mode=None,encoding='iso-8859-1')

MyQR.png('qrcode3.png',scale=8)

MyQR.show()
