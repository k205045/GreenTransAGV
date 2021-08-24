import klask
import ConncectTM as ConncectTM
from time import sleep
import My_global
from json import loads
from mbservertest import mbclient as mb

My_global._init()
Web = klask.My_app()
Web.start()



# sql = mysqlite()
mode = "Catch"
action = ""
while True:#循環開始
    try:
        # if not TM.is_alive():
        #     TM.start()
        if My_global.get_res() != None:#接收訊號後開始
            a = My_global.get_res()
            print("get_res:" + str(My_global.get_res()))
            My_global.set_res(None)
            try:
                action = a["action"] + "-" + a["start"][:3] + "-" + a["start"][5:6] + "-" + a["start"][6:] + "-" + \
                             a["end"][:3] + "-" + a["end"][5:6] + "-" + a["end"][6:]+ "-" + a["location"] + "-" + a["nolandmark"]+ "-"  + a["nobarcode"]
            except KeyError:
                action = a["action"] + "-" + a["start"][:3] + "-" + a["start"][5:6] + "-" + a["start"][6:] + "-" + \
                             a["end"][:3] + "-" + a["end"][5:6] + "-" + a["end"][6:]+ "-" + a["location"]
            if a["name"] == "action":

                mode = a['action']
                if mode == 'Home':#回原點
                    action
                elif mode == 'BARCODE':
                    action
                elif mode == 'Catch':#抓取步驟
                    if a["end"] != "":
                        My_global.set_sen({
                            "status": "PLEASE set 'end' empty"
                        })
                        continue
                    action
                elif mode == 'PUT':#擺放步驟
                    if a["start"] != "":
                        My_global.set_sen({
                            "status": "PLEASE set 'end' empty"
                        })
                        continue
                    action
                elif mode == 'OPEN':#開爪

                    action
                elif mode == 'CLOSE':#關爪

                    action
                elif mode == 'MIX':#取放連動

                    action

                    a = action.split("-")
                    print(a)
                    if a[1][:2] == "MR" or a[1][:2] == "EQ":
                        print(chr(64 + (ord(a[5])-64)*2) >= a[2][0])
                    elif a[1][:2] == "MR" or a[1][:2] == "EQ":
                        print(chr(64 + (ord(a[5]) - 64) * 2) >= a[4][0])
                elif mode == 'PLAY':#控制器開始
                    mbsev = mb()
                    b = mbsev.Play_Pause()
                    mbsev.conn.close()
                    del mbsev
                elif mode == 'PAUSE':#控制器暫停
                    mbsev = mb()
                    b = mbsev.Play_Pause()
                    mbsev.conn.close()
                    del mbsev
                elif mode == 'STOP':#控制器停止
                    mbsev = mb()
                    b = mbsev.Stop()
                    mbsev.conn.close()
                    del mbsev
                elif mode == 'CHECK':
                    action
                elif mode == 'Test':
                    action
                elif mode == 'SET':
                    action

                else:
                    print('hi')
                    print(a["name"])
                    print(a["start"][:3] + "-" + a["start"][5:]+"-"+a["end"][:3] + "-" + a["end"][5:])
                    action

                My_global.set_sen(None)
                My_global.set_sen({
                    "Result":"Y"
                })
                print("set_sen:"+str(My_global.get_sen()))
                print(action)
                TM = ConncectTM.TM(action)
                TM.start()


            elif a["name"] == "mode":
                mode = a["mode"]
                action = ''
                TM = ConncectTM.TM(mode, action)
                TM.start()
        sleep(1)
    except Exception as e:
        # print(e)
        pass








