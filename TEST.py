# from decimal import Decimal, ROUND_HALF_UP
# G_Master=['G_MASTER', '-929.63, -2.94, 260.84, -179.71, -0.54, 89.32', '-931.03, -317.21, 260.1, -179.25, 0.3, 90.25', '-1016.31, -316.57, 261.16, -179.6, 0.25, 90.27', '', '', '', '']
# L_Master=['L_MASTER', '-929.56, -2.76, 260.78, -179.62, -0.55, 89.3', '-930.98, -317.37, 260.19, -179.23, 0.41, 90.27', '-1016.21, -316.78, 261.07, -178.93, 0.18, 90.27', '', '', '', '']
# from math import sin, cos, pi
#
# M0=['-925.96', ' -3.87', ' 261.47', ' -179.55', ' -0.48', ' 89.34']
# M1=['-921.74', ' -457.79', ' 262.82', ' 179.57', ' 0.45', ' 90.16']
# c =['-925.66', '-4.28', '261.59', '-179.61', '-0.51', '89.36']
# tmp = Decimal(89.3) - Decimal(89.32)
# angle = Decimal(c[5]) - (Decimal(M0[5]) - tmp)
# angle = angle
# x = Decimal(M1[0]) * Decimal(cos(angle*Decimal(pi)/180)) + Decimal(M1[1]) * Decimal(sin(angle*Decimal(pi)/180)) - Decimal(c[0])
# y = Decimal(M1[1]) * Decimal(cos(angle*Decimal(pi)/180)) - Decimal(M1[0]) * Decimal(sin(angle*Decimal(pi)/180)) - Decimal(c[1])
#
# print("angle=" + str(angle))
#
# data = str([float(x.quantize(Decimal('.00'), ROUND_HALF_UP)), float(y.quantize(Decimal('.00'), ROUND_HALF_UP)),
# M1[2],  M1[3],  M1[4],  float(Decimal(M1[5])-Decimal(angle))]).replace("[", "{").replace("]", "}").replace("'", "")
#
# print(data)
#
#

from logger import _logging as log

k = log()
log = k.Getlogger("TM.log")
log.info("123456")









