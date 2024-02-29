import qrcode

data = "https://github.com/LucifeRsKingdoM"
qr_img = qrcode.make(data)
qr_img.save("QRCODE.png")
