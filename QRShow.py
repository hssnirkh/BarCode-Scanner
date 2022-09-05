import pyqrcode
from pyqrcode import QRCode

Dest = "https://github.com/hssnirkh"

MyQR = QRCode(Dest)

MyQR.png('qrcode2.png',scale=8)

MyQR.show()
