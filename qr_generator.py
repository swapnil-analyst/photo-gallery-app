import qrcode

url = "https://your-app-name.onrender.com"  # change after deployment

qr = qrcode.make(url)

qr.save("qr_code.png")

print("QR Code Generated!")