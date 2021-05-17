from PIL import Image, ImageDraw, ImageFilter
from PIL import ImageFont
from os import listdir
from os.path import isfile, join
mypath = "QRcodefloder"
# im = Image.open("advanceduse.png")
list = []
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print(onlyfiles)
for onlyfile in onlyfiles:
    list.append(Image.open("QRcodefloder\\"+onlyfile))




squard = list[0].size[0]
num = 0
for i in range(1,15):

    a4im = Image.new('RGB',
                     (595, 842),  # A4 at 72dpi
                     (255, 255, 255))  # White
    image2 = Image.new('RGB', (squard, squard), (0, 0, 0))
    draw = ImageDraw.Draw(a4im)
    font = ImageFont.truetype('arial.ttf', 7)
    width, height = image2.size
    print(list[0].size)
    crop_width, crop_height = a4im.size

    for left in range(0, crop_width, width):
        for top in range(0, crop_height, height):
            print(num)
            if num == len(list):
                break
            print(left,top)
            if left+squard > 595:
                break
            if top+squard > 842:
                break
            # print(left // 165)
            a4im.paste(image2, (left - left // squard, top - top // squard))
            print(left - left // squard, top - top // squard)
            a4im.paste(list[num], (left+1 - left // squard, top+1 - top // squard))
            draw.text((left + 20 - left // squard, top - top // squard), onlyfiles[num][:7], font=font, fill="#000000")

            # print(onlyfiles[num])
            num += 1


    # a4im.paste(im, im.getbbox())  # Not centered, top-left corner
    a4im.filter(ImageFilter.EDGE_ENHANCE)
    a4im.save("QR"+str(i)+".jpg", quality=100)
    a4im.show()
    if num == len(list):
        break



