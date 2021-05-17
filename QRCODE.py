import qrcode # 匯入模組


col_list = [0,0,0,0,2,2,2,4,4,4,6,6,6,8,8,8,10,10,10]
# col_list = [0,0,0,2,2,4,4,6,6,8,8,10,10]
def QRPrint(result):
    print(result)
    # qr = qrcode.QRCode(
    #     version=2,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=3,
    #     border=2,
    # )
    # qr.add_data(result)
    # qr.make(fit=True)
    # img = qr.make_image()
    # img.save("QRcodeFloder\\" + result[:7] + ".jpg")
    # qr.clear()
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=3,
    )
    qr.add_data(result)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("QRcodeFloder\\" + result[:7] + ".jpg")
    qr.clear()


def RK1Print():
    for i in range(1,5):
        RKnum = i
        for j in range(1,10):
            lanmarknum = j
            # print(lanmarknum)
            result = 'RK10'+ str(RKnum)+'-'+str(lanmarknum)
            # print(lanmarknum % 3)

            if lanmarknum == 1:
                for k in range(2,4):
                    result += '-' + chr(65+col_list[lanmarknum]) + str(k)
                for k in range(2,4):
                    result += '-' + chr(66+col_list[lanmarknum]) + str(k)
            elif lanmarknum % 3 == 1:
                for k in range(1,4):
                    result += '-' + chr(65+col_list[lanmarknum]) + str(k)
                for k in range(1,4):
                    result += '-' + chr(66+col_list[lanmarknum]) + str(k)
            elif lanmarknum % 3 == 2:
                for k in range(4,6):
                    result += '-' + chr(65+col_list[lanmarknum]) + str(k)
                for k in range(4,6):
                    result += '-' + chr(66+col_list[lanmarknum]) + str(k)
            elif lanmarknum % 3 == 0:
                for k in range(6, 8):
                    result += '-' + chr(65 + col_list[lanmarknum]) + str(k)
                for k in range(6, 8):
                    result += '-' + chr(66 + col_list[lanmarknum]) + str(k)
            # print(result)
            QRPrint(result)

def RK2Print():
    for i in range(1, 7):
        RKnum = i
        for j in range(1, 9):
            lanmarknum = j
            # print(lanmarknum)
            result = 'RK20' + str(RKnum) + '-' + str(lanmarknum)

            if lanmarknum == 7:
                for k in range(2, 4):
                    result += '-' + chr(65 + col_list[lanmarknum]) + str(k)
                for k in range(2, 4):
                    result += '-' + chr(66 + col_list[lanmarknum]) + str(k)
            elif lanmarknum % 2 == 0:
                for k in range(4, 6):
                    result += '-' + chr(65 + col_list[lanmarknum]) + str(k)
                for k in range(4, 6):
                    result += '-' + chr(66 + col_list[lanmarknum]) + str(k)
            else:
                for k in range(1, 4):
                    result += '-' + chr(65 + col_list[lanmarknum]) + str(k)
                for k in range(1, 4):
                    result += '-' + chr(66 + col_list[lanmarknum]) + str(k)
            # print(result)
            QRPrint(result)
# RK206-8
def EQ1Print():

    for i in range(11,41):
        RKnum = i
        for j in range(1,3):
            lanmarknum = j
            # print(lanmarknum)
            if RKnum > 9:
                result = 'EQ1' + str(RKnum) + '-' + str(lanmarknum)
            else:
                result = 'EQ10'+ str(RKnum) + '-' + str(lanmarknum)
            # print(lanmarknum % 3)

            if lanmarknum % 2 == 0:
                for k in range(1,4):
                    result += '-' + chr(65) + str(k)
            elif lanmarknum % 2 == 1:
                for k in range(1,4):
                    result += '-' + chr(66) + str(k)
            print(result)
            QRPrint(result)


if __name__ == '__main__':
    # RK1Print()
    # RK2Print()
    # QRPrint("EQ001-1-A1-A2-A3")
    # QRPrint("EQ001-2-B1-B2-B3")
    EQ1Print()