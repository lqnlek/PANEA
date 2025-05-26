import qrcode

# Replace this URL with your desired website
url = "https://panea.vercel.app/"

# Create QR code
qr_img = qrcode.make(url)

# Save QR code to a PNG file
qr_img.save("qr_code.png")

print("QR code saved as 'qr_code.png'")
