import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.youtube.com/watch?v=5zr88fTxsrw')
qr.make(fit=True)

img = qr.make_image(back_color=(101, 37, 196), fill_color=(238, 242, 17))
img.save("test_file2.png")