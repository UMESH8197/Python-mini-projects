# Decode a QR Code using Python
from pyzbar.pyzbar import decode
from PIL import Image 
decodeQR = decode(Image.open('instagram.png'))
print(decodeQR[0].data.decode('ascii'))
