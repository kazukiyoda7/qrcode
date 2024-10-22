import qrcode

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

for i in range(10):
    filename = str(i)+'.png'
    qr.add_data(filename)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    img.save('data/' + filename)

