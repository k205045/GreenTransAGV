#!/usr/bin/env python
# -*- coding: utf-8 -*-
# install pyModbusTCP ref: https://pypi.org/project/pyModbusTCP/
# modbus連接
# from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.compat import iteritems
from pyModbusTCP.client import ModbusClient
import time
import os
import re

class mbclient():

    def __init__(self):
        with open(os.getcwd()+"/IP.txt") as f:
            self.host = f.read().strip()
        self.port = 502
        try:
            self.conn = ModbusClient()
            # self.conn.connect()
            if not self.conn.host(self.host):
                print("host error ModbusClient not connect")
            if not self.conn.port(self.port):
                print("port error ModbusClient not connect")
            self.conn.open()
        except ValueError:
            print("ModbusClient not connect")
        print(self.conn.is_open())
        self.rule = re.compile(r'[A-Z]{2}-[A-Z0-9]{7}')


    def IAI_open(self):
        self.conn.write_single_coil(0, True)  # DO寫入
        self.conn.write_single_coil(1, False)  # DO寫入
        self.conn.write_single_coil(3, True)  # DO寫入
        self.conn.write_single_coil(4, True)  # DO寫入
        # regs = self.conn.read_coils(0, 32)  # DO讀取
        # print(regs)

    def IAI_close(self):
        self.conn.write_single_coil(0, False)  # DO寫入
        self.conn.write_single_coil(1, True)  # DO寫入
        self.conn.write_single_coil(3, True)  # DO寫入
        self.conn.write_single_coil(4, True)  # DO寫入
        # self.regs = self.conn.read_coils(0, 32)  # DO讀取
        # print(self.regs)

    def Get_Sensor(self):
        a = self.conn.read_discrete_inputs(8, 6)
        return a

    # Roboterror
    def Roboterror(self):
        return self.conn.read_discrete_inputs(7201) # FUN 02

    def M_A(self):
        self.conn.write_single_coil(7102, True)

    def Play_Pause(self):
        self.conn.write_single_coil(7104, True)

    def Stop(self):
        self.conn.write_single_coil(7105, True)

    # RoboterrorCode
    def RoboterrorCode(self):
        a = ['%02X' % i for i in self.conn.read_input_registers(7320, 2)]
        for i in range(len(a)):
            if len(a[i]) < 4:
                a[i] = "0" * (4 - len(a[i])) + a[i]
        return a[0] + a[1]

    def IAI_Error(self):
        # if self.conn.read_discrete_inputs(6) or self.conn.read_discrete_inputs(7):
        #     return True
        return False

    def GetBarcode(self):
        result = self.conn.read_holding_registers(9200, 15)
        print(result)
        # print(hex(result[0]))

        if result[0] == 0:
            return "Not Found"
        decoder = BinaryPayloadDecoder.fromRegisters(result,byteorder=Endian.Big, wordorder=Endian.Big)

        decoder = decoder.decode_string(15).decode()
        try:
            return self.rule.findall(decoder)[0]
        except:
            return "Not Found"

    def SetBarcodeCheck(self,a):
        self.conn.write_single_register(9220, int(a))
        # print(self.conn.read_holding_registers(9220, 1))




    def GetPOS(self):
        a = []
        b = 9400
        for i in range(6):
            result = self.conn.read_holding_registers(b, 32)
            # print(result.registers)
            if result.registers[0] == 0:
                return "Not Found"
            decoder = BinaryPayloadDecoder.fromRegisters(result, byteorder=Endian.Big, wordorder=Endian.Big)
            decoder = decoder.decode_string(100).decode()
            b += 32
            a.append(decoder)

        return a


    def Get_AI1(self):
        return self.conn.read_input_registers(0, 2)

    def Get_AI2(self):
        return self.conn.read_input_registers(2, 2)

    def Get_Gripper_Status(self):
        regs = self.conn.read_discrete_inputs(0, 16)  # DI讀取
        if regs[0] == True:
            return 'Fail'
        elif regs[1] == True:
            return 'Release'
        elif regs[5] == True:
            return 'Catch'

    def RobotCompelet(self):
        return self.conn.read_coils(9000)

    def home(self):
        return self.conn.read_coils(9003)

    # Error_or_Not
    def Error_or_Not(self):
        return self.conn.read_coils(9004)

    def Robotstop(self):
        return self.conn.read_input_registers(9223, 1)

    # Error_code
    def Error_code(self):
        return self.conn.read_holding_registers(9222, 1)

    def syserrorcode(self):
        return self.conn.read_holding_registers(9221, 1)

    def ErrorReset(self):
        self.conn.write_single_register(9004, 0)
        self.conn.write_single_register(9222, 0)

    # while True:
    #     # open or reconnect TCP to server
    #     if not self.conn.is_open():
    #         if not self.conn.open():
    #             print("unable to connect to "+self.host+":"+str(self.port))
    #     if self.conn.is_open():
    #
    #         # regs = self.conn.read_discrete_inputs(0, 16)#DI讀取
    #
    #         self.conn.write_single_coil(0, 0)#DO寫入
    #         self.conn.write_single_coil(1, 1)  # DO寫入
    #         self.conn.write_single_coil(3, 1)  # DO寫入
    #         self.conn.write_single_coil(4, 1)  # DO寫入
    #         regs = self.conn.read_coils(0, 32)#DO讀取
    #
    #         if regs:
    #             #write regs) to c2 address 0 (32 registers)
    #             print(regs)
    #     # sleep 2s before next polling
    #     time.sleep(2)


if __name__ == '__main__':
    import time
    a = mbclient()
    while True:
        time.sleep(1)
        print(a.GetPOS())
        # print(a.Error_code())
        # print(a.Get_Gripper_Status())

