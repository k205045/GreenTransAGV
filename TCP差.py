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
from math import sin, cos, pi, hypot
import numpy as np

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
        self.log.info(str(self.IP))
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




    def main(self):
        global M0, M1, theta
        self.TMloop = True
        if self.Disconnect == False:
            self.TMloop = False
        self.sql = sqlite_3.My_sqlite()
        self.log.info('CONNECTTM IN LOOP')
        self.tmp = {"D":"A", "C":"B", "B":"C", "A":"D"}
        print(self.ac_list)
        self.Disconnecttimes = 0
        while self.TMloop:
            if self.Disconnecttimes == 5:
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
                            self.TMloop = True
                            self.TM_str = ''
                            self.sockClient.sendall(self.SendTMSCT('var_data = "' + self.action + '"\r\nScriptExit()').encode())

                        elif a[4] == "TCPoffset":
                            self.log.info("TCPoffset")
                            Cycle = True
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_TCP)').encode())
                            while Cycle:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(b)
                                if len(a) > 3:
                                    if a[2] == '90':
                                        self.log.info(a)
                                        self.log.info(self.rule.findall(b)[0])
                                        c = self.rule.findall(b)[0]
                                        c = c.strip('{}')
                                        c = c.split(",")
                                        c = [Decimal(j) for j in c]
                                        c = [c[i:i + 2] for i in range(0, len(c), 2)]
                                        # self.log.info(c)
                                        G_circle = self.sql.Get_TM("G_MASTER")[0]
                                        G_circle = np.array([float(G_circle[1]), float(G_circle[2])])
                                        L_circle = np.array(self.getCircle(c))
                                        a = L_circle - G_circle
                                        self.log.info([float(Decimal(i).quantize(Decimal('.0000'), ROUND_HALF_UP)) for i in a])
                                        self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                                        Cycle = False
                                        self.TMloop = False
                                        self.log.info('bye')
                        elif a[4] == "GetGlobal":
                            self.log.info("GetGlobal")
                            Cycle = True
                            self.sockClient.sendall(self.SendTMSCT('ListenSend(90, var_TCP)').encode())
                            while Cycle:
                                b = self.sockClient.recv(1024).decode()
                                a = b.split(",")
                                # self.log.info(b)
                                if len(a) > 3:
                                    if a[2] == '90':
                                        self.log.info(a)
                                        self.log.info(self.rule.findall(b)[0])
                                        c = self.rule.findall(b)[0]
                                        c = c.strip('{}')
                                        c = c.split(",")
                                        c = [Decimal(j) for j in c]
                                        c = [c[i:i + 2] for i in range(0, len(c), 2)]
                                        self.log.info(c)
                                        c = self.getCircle(c)
                                        c = [float(Decimal(i).quantize(Decimal('.0000'), ROUND_HALF_UP)) for i in c]
                                        offset = ["G_MASTER"] + c
                                        if len(offset) < 9:
                                            for i in range(8 - len(offset)):
                                                offset.append('')
                                        print(offset)
                                        self.sql.Ins_TM(offset)
                                        self.sockClient.sendall(self.SendTMSCT('ScriptExit()').encode())
                                        Cycle = False
                                        self.TMloop = False
                                        self.log.info('bye')


            except socket.error as e:
                print(e)
                self.k.Del_logging()
                self.k.Getlogger("TM.log")
                self.sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sockClient.settimeout(3)
                self.sockClient.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
                with open(os.getcwd() + "\IP.txt") as f:
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
        self.sockClient.close()
        self.log.info('CONNECTTM OUT LOOP')
        self.k.Del_logging()
        sleep(0.1)

    def Average(self, lst):
        return sum(lst) / len(lst)

    def clockwise_angle(self,v1, v2):
        x1, y1 = v1
        x2, y2 = v2
        dot = float(x1 * x2 + y1 * y2)
        det = float(x1 * y2 - y1 * x2)
        theta = np.arctan2(det, dot)
        theta = theta if theta > 0 else 2 * np.pi + theta
        return theta

    def euclidean(self, p1, p2):
        _p1 = np.array([p1[0], p1[1]])
        _p2 = np.array([p2[0], p2[1]])
        p3 = p2 - p1
        return hypot(p3[0], p3[1])

    def weight(self, G1, G2):
        g1_avg = []
        g2_avg = []
        for i in range(3):
            g1_avg.append(G1[i] - G1[0])
            g2_avg.append(G2[i] - G2[0])
        g1_avg = np.mean(g1_avg, axis=0)
        g2_avg = np.mean(g2_avg, axis=0)
        return [g2_avg[0] - g1_avg[0], g2_avg[1] - g1_avg[1]]

    def getCircle(self, c):
        K_1 = -(c[1][0] - c[0][0]) / (c[1][1] - c[0][1])
        K_2 = -(c[2][0] - c[1][0]) / (c[2][1] - c[1][1])
        x1 = (c[1][0] + c[0][0]) / Decimal("2")
        x2 = (c[2][0] + c[1][0]) / Decimal("2")
        y1 = (c[1][1] + c[0][1]) / Decimal("2")
        y2 = (c[2][1] + c[1][1]) / Decimal("2")
        x = np.array([[K_1, Decimal("-1")], [K_2, Decimal("-1")]], dtype='float')
        y = np.array([K_1 * x1 - y1, K_2 * x2 - y2], dtype='float')
        return np.dot(np.linalg.inv(x), y).tolist()

if __name__ == '__main__':
    while True:
        b = input()
        a = TM(b, "123")
        a.main()



