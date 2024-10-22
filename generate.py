import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
    mask_pattern=0
)

for i in range(10):
    data = str(i)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    img.save('data/' + data + '.png')

    qr.clear()
