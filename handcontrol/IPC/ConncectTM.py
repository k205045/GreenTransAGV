import socket
from time import sleep
from threading import Thread
import re
from decimal import Decimal
import sqlite_3
import GTAGV
import sys
# from PySide2.QtWidgets import QApplication
import My_global
import os
from logger import _logging as log

class TM(Thread):
    def __init__(self, action, mode=''):
        Thread.__init__(self)
        self.k = log()
        self.log = self.k.Getlogger("TM.log")
        # self.rule = re.compile(r"[A-Z]+/-}")
        self.rule = re.compile(r"{.+}")
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
        try:
            # self.sockClient.connect(('localhost', 5890))
            self.sockClient.connect((self.IP, 5890))
            self.Disconnect = True
        except:
            self.Disconnect = False
            self.log.info("Robot Not Connect!")

    def xor_strings(self, rulsult):
        self.log.info(rulsult)
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
        self.TMloop = True
        if self.Disconnect == False:
            self.TMloop = False
        self.sql = sqlite_3.My_sqlite()
        self.log.info('CONNECTTM IN LOOP')
        while self.TMloop:
            # print("============")
            sleep(0.5)
            try:
                offset = []
                self.sockClient.sendall("$TMSTA,2,00,*41\r\n".encode())
                a = self.sockClient.recv(1024).decode().split(",")
                # a = [0,0,0,"true","Start"]
                if a[0] != "" or len(a) > -1:
                    # print(a)
                    if a[3] == "true":
                        if a[4] == "Start":

                            if self.mode == "HOME" or self.mode == "BARCODE" or self.mode == "CHECK":
                                self.sockClient.sendall(self.SendTMSCT('var_Start = "' + self.mode + '"\r\nScriptExit()').encode())
                            elif self.mode == "BARCODE":
                                self.log.info(1)
                                self.sockClient.sendall(
                                    self.SendTMSCT('var_Start = "' + self.mode + '"\r\nScriptExit()').encode())



                            # else:
                            #     self.sockClient.sendall(self.SendTMSCT('var_test = "' + str(self.action) + '"\r\nScriptExit()').encode())
                            #     self.log.info('var_test = "' + str(self.action) + '"\r\nScriptExit()')


                            self.TMloop = False
                            if self.mode == "SET":
                                self.TMloop = True
                                self.TM_str = ''
                                self.sockClient.sendall(self.SendTMSCT('var_data = "' + self.action +'"\r\nScriptExit()').encode())
                            elif self.mode == "PUT" or self.mode == "Catch" or self.mode == "MIX":

                                self.TMloop = True
                                self.sockClient.sendall(self.SendTMSCT(
                                    'var_data = "' + self.action + '"\r\nScriptExit()').encode())
                                print(self.sockClient.recv(1024).decode())
                                # app = QApplication(sys.argv)
                                # Login_1 = GTAGV.GTAGV()
                                # Login_1.show()
                                # app.exec_()
                                # self.data = Login_1.data
                                # for i in self.data:
                                #     self.TM_str = self.TM_str + ',' + i
                                # self.sockClient.sendall(self.SendTMSCT('var_locate = "' + self.TM_str + '"').encode())

                        if a[4] == "give_pos_data":
                            self.log.info("give_pos_data")
                            Cycle = True
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_alllllllll)\r\nScriptExit()').encode())
                            while Cycle:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(a)
                                if a[2] == '90':
                                    self.log.info(a)
                                    self.log.info(self.rule.findall(b)[0])
                                    c = self.rule.findall(b)[0]
                                    c = [i.split(",") for i in c.replace("}", "").split("{")]
                                    # self.log.info(c)
                                    c.pop(0)
                                    self.log.info(c)
                                    if c[0][0] == "":
                                        raise Exception("QRCODE NOT FOUND")
                                    else:
                                        offset.append(c[0][0])
                                    for j in range(2, len(c)):
                                        # print(j)
                                        print(c[j])
                                        offset.append(
                                            str([float(Decimal(c[1][i]) - Decimal(c[j][i])) for i in
                                                 range(0, len(c[1]))]).
                                                replace('[', "").replace(']', ''))
                                    # self.log.info(len(offset))
                                    if len(offset) < 7:
                                        for i in range(7 - len(offset)):
                                            offset.append('')
                                    self.log.info(offset)
                                    # os.makedirs(os.getcwd()+'\\pos', exist_ok=True)
                                    # with open(os.getcwd()+'\\pos\\'+c[0][0] + '.txt','w+') as f:
                                    #     f.write(str(offset).strip("['']"))
                                    self.sql.Ins_TM(offset)
                                    Cycle = False
                            # sleep(3)
                            # self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                            # print(self.sockClient.recv(1024))
                            self.TMloop = False
                            self.log.info('bye')
                        if a[4] == "give_pos_data_2":
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_allpos)').encode())
                            while True:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(a)
                                if a[2] == '90':
                                    # self.log.info(b)
                                    c = self.rule.findall(b)[0]
                                    self.log.info(c)
                                    c = c.replace("}", "").split("{")
                                    c[1] = c[1].split(",")
                                    c.pop(0)
                                    self.log.info(c)
                                    # if os.path.isfile(os.getcwd()+'\\pos\\'+c[0] + '.txt'):
                                    #     with open(os.getcwd()+'\\pos\\'+c[0][0] + '.txt','r') as f:
                                    #         d = f.read().split(',')
                                    #         e = []
                                    #         f = []
                                    #         k = 1
                                    #         for i in range(len(d)):
                                    #             e.append(d[i])
                                    #             if k % 6 == 0:
                                    #                 f.append(e)
                                    #                 e = []
                                    #             k += 1
                                    # else:
                                    #     My_global.set_error(str(e))
                                    #     while True:
                                    #         if My_global.get_error() == None:
                                    #             break
                                    #         sleep(0.5)
                                    try:

                                        # d = self.sql.Get_TM(c[0][0])[0][int(self.ac_list[1])]
                                        if self.ac_list[1][:2] == "MR" or self.ac_list[1][:2] == "EQ":
                                            if self.ac_list[2] == "A01":
                                                self.pos = 1
                                            elif self.ac_list[2] == "A02":
                                                self.pos = 2
                                            elif self.ac_list[2] == "A03":
                                                self.pos = 3
                                        elif self.ac_list[1][:2] == "MR" or self.ac_list[1][:2] == "EQ":
                                            if self.ac_list[4] == "A01":
                                                self.pos = 1
                                            elif self.ac_list[4] == "A02":
                                                self.pos = 2
                                            elif self.ac_list[4] == "A03":
                                                self.pos = 3
                                        print(self.pos)
                                        d = self.sql.Get_TM(c[0][0])[0][self.pos]

                                    except Exception as e:
                                        # print(e)
                                        My_global.set_error(str(e))
                                        while True:
                                            if My_global.get_error() == None:
                                                break
                                            sleep(0.5)
                                    d = d.split(",")
                                    c = c[1].split(",")
                                    self.log.info(d)
                                    self.log.info(c)
                                    data = str([float(Decimal(c[i]) - Decimal(d[i])) for i in range(0, len(d))]).\
                                        replace("[", "{").replace("]", "}")
                                    self.log.info("data" + data)
                                    break

                            self.sockClient.sendall(self.SendTMSCT('var_Hugh = ' + data +'\r\nScriptExit()').encode())
                            print('var_Hugh = ' + data +'\r\nScriptExit()')
                            for i in range(3):
                                print(self.sockClient.recv(1024).decode())
                            self.TMloop = False

            except socket.error:
                break
            except Exception as e:
                self.log.info(e)
                # self.log.info('var_test = "' + str(self.action) + '"\r\nScriptExit()')
                break
        self.sockClient.close()
        self.k.Del_logging()
        self.log.info('CONNECTTM OUT LOOP')
        sleep(0.1)


if __name__ == '__main__':
    a = TM("Catch","123")
    a.start()



