import qrcode
import image


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = "Renas AYIN"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(back_color="white", fill_color="black")

img.save("yusfu.png")
