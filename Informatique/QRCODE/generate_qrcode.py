import qrcode  # Import the qrcode library
url = "https://julien35235.github.io/CV/Mon_CV/index.html"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("cv_julien_qrcode.png")
print("QR code generated successfully.")