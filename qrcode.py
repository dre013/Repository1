import qrcode
img = qrcode.make('https://www.youtube.com/watch?v=0TyvWoVW2Ss')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")