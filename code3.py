# Before you start, install this mudule : pip install qrcode[pil]   
import qrcode

url = input("Enter the URL:").strip()
file_path = r"C:\\Users\\Subham\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Your qr code is ready!!")