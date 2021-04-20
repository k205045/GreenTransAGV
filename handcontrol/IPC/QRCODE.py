import qrcode # 匯入模組
qr = qrcode.QRCode(
version=2,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=5,
border=2,
)
qr.add_data('RK101-1')
qr.make(fit=True)
img = qr.make_image()
img.save("advanceduse.png")