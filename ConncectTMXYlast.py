# pyinstaller --hidden-import=scipy._lib.messagestream myscript.py
import socket
from time import sleep
from threading import Thread
import re
from decimal import Decimal, ROUND_HALF_UP
import sqlite_3
import mbservertest
# from PySide2.QtWidgets import QApplication
import My_global
import os
from logger import _logging as log
from math import sin, cos, pi
class TM(Thread):
    def __init__(self, action, mode=''):
        Thread.__init__(self)
        self.k = log()
        self.log = self.k.Getlogger("TM.log")
        # self.rule = re.compile(r"[A-Z]+/-}")
        self.rule = re.compile(r"{.+}")
        self.rule1 = re.compile(r"d+")
        self.rule2 = re.compile(r"[A-Z]+")
        self.rulelist = action.split('-')
        self.log.info(self.rulelist)
        self.mode = self.rulelist[0]
        # self.action = self.rulelist[1]
        self.action = action
        self.ac_list = self.action.split("-")
        self.log.info([self.action,self.mode])
        self.sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockClient.settimeout(3)
        self.sockClient.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
        with open(os.getcwd()+"/IP.txt") as f:
            self.IP = f.read().strip()
        self.IP = 'localhost'
        try:
            # self.sockClient.connect(('localhost', 5890))
            self.sockClient.connect((self.IP, 5890))
            self.Disconnect = True
        except:
            self.Disconnect = False
            self.log.info("Robot Not Connect!")

    def xor_strings(self, rulsult):
        # self.log.info(rulsult)
        tmp = ord(rulsult[0])
        for i in range(1, len(rulsult)):
            tmp = tmp ^ ord(rulsult[i])

        if len(hex(tmp)[2:]) == 1:
            return "0" + str(hex(tmp))[2:]

        return str(hex(tmp))[2:]

    def SendTMSCT(self, data): #Listen
        ID = str(0)
        Len = str(1 + len(ID) + len(data))
        cmd = "TMSCT," + Len + ",0," + data + ","
        checksum = self.xor_strings(cmd)
        self.log.info("$" + cmd + "*" + checksum + "\r\n")
        return "$" + cmd + "*" + checksum + "\r\n"




    def run(self):
        global M0, M1
        self.TMloop = True
        if self.Disconnect == False:
            self.TMloop = False
        self.sql = sqlite_3.My_sqlite()
        self.log.info('CONNECTTM IN LOOP')
        self.tmp = {"D":"A", "C":"B", "B":"C", "A":"D"}
        print(self.ac_list)
        if self.ac_list[7] == "Z":
            pass
        else:
            if self.ac_list[1][:2] == "RK" or self.ac_list[1][:2] == "EQ":

                if self.ac_list[1][:2] == "RK":
                    if self.ac_list[1][:3] == "RK1":

                        if int(self.ac_list[3]) > 3:
                            if not 2 * ord(self.tmp[self.ac_list[7]]) - 66 <= ord(self.ac_list[2]) + 1 <= 2 * ord(
                                    self.tmp[self.ac_list[7]]) - 65:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                        else:
                            if not 2 * ord(self.tmp[self.ac_list[7]]) - 65 <= ord(self.ac_list[2]) \
                                   <= 2 * ord(self.tmp[self.ac_list[7]]) - 64:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                    else:

                        if int(self.ac_list[3]) > 3:
                            if not 2 * ord(self.ac_list[7]) - 66 <= ord(self.ac_list[2]) + 1 <= 2 * ord(
                                    self.ac_list[7]) - 65:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                        else:
                            if not 2 * ord(self.ac_list[7]) - 65 <= ord(self.ac_list[2]) <= 2 * ord(self.ac_list[7]) - 64:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False

                else:
                    if self.ac_list[7] != self.ac_list[2]:
                        self.log.info("停車點與夾取點不相符")
                        self.TMloop = False

            elif self.ac_list[4][:2] == "RK" or self.ac_list[4][:2] == "EQ":

                if self.ac_list[4][:2] == "RK":
                    if self.ac_list[4][:3] == "RK1":
                        if int(self.ac_list[6]) > 3:
                            if not 2 * ord(self.tmp[self.ac_list[7]]) - 66 <= ord(self.ac_list[5]) + 1 <= 2 * ord(
                                    self.tmp[self.ac_list[7]]) - 65:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                        else:
                            if not 2 * ord(self.tmp[self.ac_list[7]]) - 65 <= ord(self.ac_list[5]) \
                                   <= 2 * ord(self.tmp[self.ac_list[7]]) - 64:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                    else:

                        if int(self.ac_list[6]) > 3:
                            if not 2 * ord(self.ac_list[7]) - 66 <= ord(self.ac_list[5]) + 1 <= 2 * ord(
                                    self.ac_list[7]) - 65:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                        else:
                            if not 2 * ord(self.ac_list[7]) - 65 <= ord(self.ac_list[5]) <= 2 * ord(self.ac_list[7]) - 64:
                                self.log.info("停車點與夾取點不相符")
                                self.TMloop = False
                else:
                    if self.ac_list[7] != self.ac_list[5]:
                        self.log.info("停車點與夾取點不相符")
                        self.TMloop = False
            else:
                self.log.info("參數錯誤")
                self.TMloop = False
        self.Disconnecttimes = 0
        mbsev = mbservertest.mbclient()
        while self.TMloop:
            if self.Disconnecttimes == 5:
                self.TMloop = False
            if mbsev.Robotstop() == 0 or mbsev.Robotstop() == None:
                self.TMloop = False
            # print("============")
            try:
                sleep(0.5)
                # try:
                offset = []
                self.sockClient.sendall("$TMSTA,2,00,*41\r\n".encode())
                a_1 = self.sockClient.recv(1024).decode()
                a = a_1.split(",")
                # a = [0,0,0,"true","Start"]
                if a_1.strip() != "" or len(a) == 6:
                    # print(a)
                    if a[3] == "true":
                        if a[4] == "Start":

                            if self.mode == "HOME" or self.mode == "BARCODE" or self.mode == "CHECK":
                                self.sockClient.sendall(self.SendTMSCT('var_data = "' + self.action + '"\r\nScriptExit()').encode())
                            elif self.mode == "BARCODE":
                                # self.log.info(1)
                                self.sockClient.sendall(
                                    self.SendTMSCT('var_data = "' + self.action + '"\r\nScriptExit()').encode())



                            # else:
                            #     self.sockClient.sendall(self.SendTMSCT('var_test = "' + str(self.action) + '"\r\nScriptExit()').encode())
                            #     self.log.info('var_test = "' + str(self.action) + '"\r\nScriptExit()')


                            self.TMloop = False
                            if self.mode == "SET" or self.mode == "SET_G_MASTER" or self.mode == "SET_L_MASTER":
                                self.TMloop = True
                                self.TM_str = ''
                                self.sockClient.sendall(self.SendTMSCT('var_data = "' + self.action +'"\r\nScriptExit()').encode())
                            elif self.mode == "PUT" or self.mode == "Catch" or self.mode == "MIX" :

                                self.TMloop = True
                                self.sockClient.sendall(self.SendTMSCT(
                                    'var_data = "' + self.action + '"\r\nScriptExit()').encode())


                                # print(self.sockClient.recv(1024).decode())
                                # print(self.sockClient.recv(1024).decode())
                                # print(self.sockClient.recv(1024).decode())
                                # print(self.sockClient.recv(1024).decode())
                                # app = QApplication(sys.argv)
                                # Login_1 = GTAGV.GTAGV()
                                # Login_1.show()
                                # app.exec_()
                                # self.data = Login_1.data
                                # for i in self.data:
                                #     self.TM_str = self.TM_str + ',' + i
                                # self.sockClient.sendall(self.SendTMSCT('var_locate = "' + self.TM_str + '"').encode())

                        elif a[4] == "give_pos_data":
                            self.log.info("give_pos_data")
                            Cycle = True
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_allpos)').encode())
                            while Cycle:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(b)
                                if len(a) > 3:
                                    if a[2] == '90':
                                        self.log.info(a)
                                        self.log.info(self.rule.findall(b)[0])
                                        c = self.rule.findall(b)[0]
                                        c = c.replace("}","").split("{")
                                        c = [i.split(",") for i in c]
                                        # self.log.info(c)
                                        c.pop(0)
                                        self.log.info(c)
                                        if c[0][0] == "":
                                            raise Exception("QRCODE NOT FOUND")
                                        else:
                                            offset.append(c[0][0])

                                        for i in range(1,len(c)):
                                            offset.append(str(c[i]).
                                                        replace('[', "").replace(']', '').replace("'",""))

                                        # for j in range(2, len(c)):
                                        #     # print(j)
                                        #     print(c[j])
                                        #     if c[j][0] == '':
                                        #         offset.append("")
                                        #     else:
                                        #         offset.append(
                                        #             str([float(Decimal(c[1][i]) - Decimal(c[j][i])) for i in
                                        #                  range(len(c[1]))]).
                                        #                 replace('[', "").replace(']', ''))
                                        self.log.info(offset)
                                        if len(offset) < 9:
                                            for i in range(8 - len(offset)):
                                                offset.append('')

                                        self.log.info(offset)
                                        # os.makedirs(os.getcwd()+'\\pos', exist_ok=True)
                                        # with open(os.getcwd()+'\\pos\\'+c[0][0] + '.txt','w+') as f:
                                        #     f.write(str(offset).strip("['']"))
                                        self.sql.Ins_TM(offset)
                                        self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                                        Cycle = False
                            # sleep(3)
                            # self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                            # print(self.sockClient.recv(1024))
                            self.TMloop = False
                            self.log.info('bye')
                        elif a[4] == "give_pos_data_2":
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_allpos)').encode())
                            while True:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(a)
                                if len(a) > 3:
                                    if a[2] == '90':
                                        self.log.info(b)
                                        c = self.rule.findall(b)[0]
                                        self.log.info(c)
                                        c = c.replace("}", "").split("{")
                                        c.pop(0)
                                        c[1] = c[1].split(",")

                                        self.log.info(c)
                                        print(self.ac_list)
                                        try:
                                            RK1_1 = [0, 8, 9, 10, 1, 2, 3 ]
                                            RK1_2 = [0, 11, 12, 4, 5]
                                            RK1_3 = [0,13, 14, 6, 7]
                                            RK2_1 = [0, 1, 2, 3, 6, 7, 8]
                                            RK2_2 = [0, 4, 5, 9, 10]

                                            # d = self.sql.Get_TM(c[0][0])[0][int(self.ac_list[1])]
                                            if self.ac_list[1][:2] == "RK" or self.ac_list[1][:2] == "EQ":
                                                self.tmp = int(self.ac_list[3])
                                                self.tmp1 = (ord(self.ac_list[2]) - 65) % 2
                                                if self.ac_list[1][:2] == "RK":
                                                    if self.ac_list[1][:3] == "RK1":
                                                            try:
                                                                self.pos = RK1_1.index(self.tmp1 * 7 + self.tmp)
                                                            except:
                                                                try:
                                                                    self.pos = RK1_2.index(self.tmp1 * 7 + self.tmp)
                                                                except:
                                                                    self.pos = RK1_3.index(self.tmp1 * 7 + self.tmp)
                                                    else:
                                                        try:
                                                            self.pos = RK2_1.index(self.tmp1 * 5 + self.tmp)
                                                        except:
                                                            self.pos = RK2_2.index(self.tmp1 * 5 + self.tmp)
                                                else:
                                                    self.pos = self.tmp

                                            elif self.ac_list[4][:2] == "RK" or self.ac_list[4][:2] == "EQ":
                                                self.tmp = int(self.ac_list[6])
                                                self.tmp1 = (ord(self.ac_list[5]) - 65) % 2
                                                if self.ac_list[4][:2] == "RK":
                                                    if self.ac_list[4][:3] == "RK1":
                                                        try:
                                                            self.pos = RK1_1.index(self.tmp1 * 7 + self.tmp)
                                                        except:
                                                            try:
                                                                self.pos = RK1_2.index(self.tmp1 * 7 + self.tmp)
                                                            except:
                                                                self.pos = RK1_3.index(self.tmp1 * 7 + self.tmp)
                                                    else:
                                                        try:
                                                            self.pos = RK2_1.index(self.tmp1 * 5 + self.tmp)
                                                        except:
                                                            self.pos = RK2_2.index(self.tmp1 * 5 + self.tmp)
                                                else:
                                                    self.pos = self.tmp

                                            self.log.info(self.tmp1 * 7 + self.tmp)
                                            print(c[0])
                                            M1 = self.sql.Get_TM(c[0])[0][self.pos+1]
                                            M0 = self.sql.Get_TM(c[0])[0][1]
                                            G_Master = self.sql.Get_TM("G_Master")[0]
                                            L_Master = self.sql.Get_TM("L_Master")[0]
                                        except Exception as e:
                                            print(e)
                                            My_global.set_error(str(e))
                                            while True:
                                                if My_global.get_error() == None:
                                                    break
                                                sleep(0.5)
                                        self.log.info(str(M1))
                                        self.log.info(str(self.pos+1))
                                        if M1:
                                            M1 = M1.split(",")
                                            M0 = M0.split(",")
                                            c = c[1]
                                            _G_Master = ["", "", ""]
                                            _G_Master[0] = G_Master[1].split(",")
                                            _G_Master[1] = G_Master[2].split(",")
                                            _G_Master[2] = G_Master[3].split(",")
                                            _L_Master = ["", "", ""]
                                            _L_Master[0] = L_Master[1].split(",")
                                            _L_Master[1] = L_Master[2].split(",")
                                            _L_Master[2] = L_Master[3].split(",")
                                            self.log.info("G_Master=" + str(G_Master))
                                            self.log.info("L_Master=" + str(L_Master))

                                            self.log.info("M0="+str(M0))
                                            self.log.info("M1="+str(M1))
                                            self.log.info("M0'="+str(c))
                                            # data = str([float(Decimal(c[i]) - Decimal(d[i])) for i in range(0, len(d))]).\
                                            #     replace("[", "{").replace("]", "}")

                                            tmp_z = []
                                            tmp_x = []
                                            tmp_y = []
                                            for i in range(0, 3):
                                                tmp_z.append(Decimal(Decimal(_L_Master[i][5] - _G_Master[i][5])))
                                                tmp_x.append(Decimal(Decimal(_L_Master[i][0] - _G_Master[i][0])))
                                                tmp_y.append(Decimal(Decimal(_L_Master[i][1] - _G_Master[i][2])))
                                            tmp_z = self.Average(tmp_z)
                                            tmp_x = self.Average(tmp_x)
                                            tmp_y = self.Average(tmp_y)
                                            self.log.info('tmp_z='+str(tmp_z))
                                            self.log.info('tmp_x='+str(tmp_x))
                                            self.log.info('tmp_y='+str(tmp_y))
                                            self.log.info("M0-M0'=" + str(Decimal(M0[5]) - Decimal(c[5])))


                                            # angle = Decimal(11)
                                            # f = Decimal(M0[0]) * Decimal(cos(tmp * Decimal(pi) / 180)) + Decimal(M0[1]) * Decimal(sin(tmp * Decimal(pi) / 180))
                                            # g = Decimal(M0[1]) * Decimal(cos(tmp * Decimal(pi) / 180)) - Decimal(M0[0]) * Decimal(sin(tmp * Decimal(pi) / 180))
                                            # M0[1]*cos(tmp)-M0[0]*sin(tmp)-c[1]

                                            # M0_rotate = [float(f.quantize(Decimal('.00'), ROUND_HALF_UP)),
                                            #      float(g.quantize(Decimal('.00'), ROUND_HALF_UP)),
                                            #      M0[2], M0[3], M0[4], float(Decimal(M0[5]) - Decimal(tmp))]
                                            # self.log.info("M0_rotate-M0'=" + str(Decimal(M0_rotate[5])) - Decimal(c[5]))

                                            angle = Decimal(c[5]) - (Decimal(M0[5]) - tmp_z)

                                            x = Decimal(M1[0]) * Decimal(cos(angle*Decimal(pi)/180)) + Decimal(M1[1]) * \
                                                Decimal(sin(angle*Decimal(pi)/180)) - Decimal(c[0]) - tmp_x
                                            y = Decimal(M1[1]) * Decimal(cos(angle*Decimal(pi)/180)) - Decimal(M1[0]) * \
                                                Decimal(sin(angle*Decimal(pi)/180)) - Decimal(c[1]) - tmp_y
                                            # x = (Decimal(M1[0]) - Decimal(M0[0])) + Decimal(c[0])
                                            # y = (Decimal(M1[1]) - Decimal(M0[1])) + Decimal(c[1])

                                            # print("------")
                                            # print(str(M1[1]))
                                            # print(str(cos(angle)))
                                            # print(str(M1[0]))
                                            # print(str(sin(angle)))
                                            # print(str(Decimal(M0[1]) -  Decimal(c[1])))
                                            # print("------")
                                            self.log.info("angle=" + str(angle))

                                            data = str([float(x.quantize(Decimal('.00'), ROUND_HALF_UP)), float(y.quantize(Decimal('.00'), ROUND_HALF_UP)),
                                                        M1[2],  M1[3],  M1[4],  float(Decimal(M1[5])-Decimal(angle))]).replace("[", "{").replace("]", "}").replace("'", "")

                                            self.log.info("data" + data)
                                        else:
                                            data = ''
                                            self.log.info("找不到輸入的QRcode")
                                        break
                            # sleep(0.5)
                            self.sockClient.sendall(self.SendTMSCT('var_targetpos = ' + data +'\r\nScriptExit()').encode())
                            # self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                            print('var_targetpos = ' + data +'\r\nScriptExit()')
                            print(self.sockClient.recv(1024).decode())
                            self.TMloop = False
            except socket.error as e:
                print(e)
                self.k.Del_logging()
                self.sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sockClient.settimeout(3)
                self.sockClient.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
                with open(os.getcwd() + "/IP.txt") as f:
                    self.IP = f.read().strip()
                try:
                    # self.sockClient.connect(('localhost', 5890))
                    self.Disconnecttimes = 0
                    self.sockClient.connect((self.IP, 5890))
                    self.Disconnect = True
                except:
                    self.Disconnecttimes += 1
                    self.Disconnect = False
                    self.log.info("Robot Not Connect!")




            # except socket.error:
            #     break
            # except Exception as e:
            #     self.log.info(e)
            #     # self.log.info('var_test = "' + str(self.action) + '"\r\nScriptExit()')
            #     break
        mbsev.conn.close()
        self.sockClient.close()
        self.log.info('CONNECTTM OUT LOOP')
        self.k.Del_logging()
        sleep(0.1)

    def Average(self, lst):
        return sum(lst) / len(lst)

if __name__ == '__main__':
    a = TM("Catch","123")
    a.start()



