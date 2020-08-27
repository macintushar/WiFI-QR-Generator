import pyqrcode 
import png 
from pyqrcode import QRCode 
import os  
from PIL import Image
import time  

txt = input("Enter the text to generate a QR Code for: \n")
s = txt

url = pyqrcode.create(s) 
url.png('qr.png', scale = 6) 

img = Image.open("qr.png")
img.show()
print('This image will delete in 5 Seconds :)')
time.sleep(5)
os.remove('qr.png')