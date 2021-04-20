import math
from decimal import Decimal, ROUND_HALF_UP
import numpy as np
import sqlite_3
sql = sqlite_3.My_sqlite()
# global_1 = [[-1136.24,-73.31,51.94,179.98,0.09,88.84],[-1141.01,-339.36,51.62,-179.57,0.02,88.95],
#             [-1227.59,-337.44,51.68,-179.79,0.18,88.99]]
#
# global_2 = [[-1141.95, -76.56, 50.7, -179.79, 0.21, 88.97],[-1145.71, -343, 50.27, -179.46, -0.45, 89.09],
#             [-1232.21, -341.57, 50.19, -179.71, 0.09, 89.14]]

def clockwise_angle(v1, v2):
    x1,y1 = v1
    x2,y2 = v2
    dot = float(x1*x2+y1*y2)
    det = float(x1*y2-y1*x2)
    theta = np.arctan2(det, dot)
    theta = theta if theta>0 else 2*np.pi+theta
    return theta



global_1_1 = sql.Get_TM_all("G_Master")[0]
global_2_1 = sql.Get_TM_all("L_Master")[0]

print(global_2_1)

for i in range(4):
    global_1_1.pop(3)
for i in range(4):
    global_2_1.pop(3)
global_1 = ["", "", ""]
global_1[0] = global_1_1[0].split(",")
global_1[1] = global_1_1[1].split(",")
global_1[2] = global_1_1[2].split(",")
global_2 = ["", "", ""]
global_2[0] = global_2_1[0].split(",")
global_2[1] = global_2_1[1].split(",")
global_2[2] = global_2_1[2].split(",")

print(global_1)

for i in range(len(global_1)):
    for j in range(len(global_1[i])):
        if j < 3:
            global_1[i][j] = Decimal(global_1[i][j]) - Decimal(global_1[0][j])
        else:
            if Decimal(global_1[i][j]) < 0:
                global_1[i][j] = Decimal(global_1[i][j]) + Decimal(360)
            else:
                global_1[i][j] = Decimal(global_1[i][j])
for i in range(len(global_2)):
    for j in range(len(global_2[i])):
        if j < 3:
            global_2[i][j] = Decimal(global_2[i][j]) - Decimal(global_2[0][j])
        else:
            if Decimal(global_2[i][j]) < 0:
                global_2[i][j] = Decimal(global_2[i][j]) + Decimal(360)
            else:
                global_2[i][j] = Decimal(global_2[i][j])

global_1 = np.array(global_1)
global_2 = np.array(global_2)
print(global_1)
print(global_2)
print(
"------------------------------------------------------------------------")

# v1_1 = global_1[0] - global_1[1]
# for j in range(len(v1_1)):
#     if Decimal(v1_1[j]) < 0:
#         v1_1[j] = Decimal(v1_1[j]) + Decimal(360)
#     else:
#         v1_1[j] = Decimal(v1_1[j])
#
# print("V1", v1_1)
# print(
# "------------------------------------------------------------------------")
# v2_1 = global_2[0] - global_2[1]
# for j in range(len(v2_1)):
#     if Decimal(v2_1[j]) < 0:
#       v2_1[j] = Decimal(v2_1[j]) + Decimal(360)
#     else:
#       v2_1[j] = Decimal(v2_1[j])
#
# print("V2", v2_1)
# V1 = [v1_1[0], v1_1[1]]
# V2 = [v2_1[0], v2_1[1]]
# theta = clockwise_angle(V1, V2)
# print(
# "------------------------------------------------------------------------")
# print("theta", theta * 180 / np.pi)
#
# a = global_1[0] - global_2[0]
#
# b = global_1[1] - global_2[1]
#
# c = global_1[2] - global_2[2]
#
# print(a, b, c)
#
# for i in range(2):
#     if abs(a[i] - b[i]) > Decimal("0.8"):
#         print("hia")
#     if abs(b[i] - c[i]) > Decimal("0.8"):
#         print("hib")
#     if abs(c[i] - a[i]) > Decimal("0.8"):
#         print("hic")
#
# a = np.array([a,b,c])
# print("__________________")
# print(np.mean(a, axis=0))
# print("__________________")
#
#
#
# for i in range(len(global_1)):
#     for j in range(len(global_1[i])):
#         if j < 3:
#             global_1[i][j] = Decimal(global_1[i][j])
#         else:
#             if Decimal(global_1[i][j]) < 0:
#                 global_1[i][j] = Decimal(global_1[i][j]) + Decimal(360)
#             else:
#                 global_1[i][j] = Decimal(global_1[i][j])
# for i in range(len(global_2)):
#     for j in range(len(global_2[i])):
#         if j < 3:
#             global_2[i][j] = Decimal(global_2[i][j])
#         else:
#             if Decimal(global_2[i][j]) < 0:
#                 global_2[i][j] = Decimal(global_2[i][j]) + Decimal(360)
#             else:
#                 global_2[i][j] = Decimal(global_2[i][j])
#
# global_1 = np.array(global_1)
# global_2 = np.array(global_2)
# print(global_1)
# print("------------------------------------------------------------------------")
# print(global_2)
#
# print("------------------------------------------------------------------------")
#
# v1_1 = global_1[0] - global_1[1]
# for j in range(len(v1_1)):
#     if Decimal(v1_1[j]) < 0:
#         v1_1[j] = Decimal(v1_1[j]) + Decimal(360)
#     else:
#         v1_1[j] = Decimal(v1_1[j])
#
# print("V1",v1_1)
# print("------------------------------------------------------------------------")
# v2_1 = global_2[0] - global_2[1]
# for j in range(len(v2_1)):
#     if Decimal(v2_1[j]) < 0:
#         v2_1[j] = Decimal(v2_1[j]) + Decimal(360)
#     else:
#         v2_1[j] = Decimal(v2_1[j])
#
# print("V2",v2_1)
# V1 = [v1_1[0],v1_1[1]]
# V2 = [v2_1[0],v2_1[1]]
# theta = clockwise_angle(V1,V2)
# print("------------------------------------------------------------------------")
# print("theta",theta*180/np.pi)
# print("------------------------------------------------------------------------")
# # for i in range(3):
# d_global = global_1-global_2
# # # print(global_1-global_2)
# for i in range(len(d_global)):
#     for j in range(len(d_global[i])):
#         if Decimal(d_global[i][j]) < 0:
#             d_global[i][j] = Decimal(d_global[i][j]) + Decimal(360)
#         else:
#             d_global[i][j] = Decimal(d_global[i][j])
# print(d_global)
# # print(math.hypot(p3[0][1],p3[]))
# print("------------------------------------------------------------------------")
# def euclidean(p1, p2):
#     _p1 = np.array([p1[0], p1[1]])
#     _p2 = np.array([p2[0], p2[1]])
#     p3 = p2 - p1
#     return math.hypot(p3[0], p3[1])
#
# def weight(G1,G2):
#     g1_avg = []
#     g2_avg = []
#     for i in range(3):
#         g1_avg.append(G1[i] - G1[0])
#         g2_avg.append(G2[i] - G2[0])
#     g1_avg = np.mean(g1_avg, axis=0)
#     g2_avg = np.mean(g2_avg, axis=0)
#     return [g2_avg[0]-g1_avg[0], g2_avg[1]-g1_avg[1]]
#
# print(weight(global_1,global_2))
#
# for i in range(3):
#     print(chr(65+i))
#     if i != 2:
#         # print(euclidean(global_1[i][0],global_1[i+1][0],global_1[i][1],global_1[i+1][1]))
#         # print(euclidean(global_2[i][0],global_2[i+1][0],global_2[i][1],global_2[i+1][1]))
#         print(euclidean(global_1[i], global_1[i + 1]))
#         print(euclidean(global_2[i], global_2[i + 1]))
#
#         print("------------------------------------------------------------------------")
#     else:
#         # print(euclidean(global_1[i][0], global_1[i - 2][0], global_1[i][1], global_1[i - 2][1]))
#         # print(euclidean(global_2[i][0], global_2[i - 2][0], global_2[i][1], global_2[i - 2][1]))
#         print(euclidean(global_1[i], global_1[i - 2]))
#         print(euclidean(global_2[i], global_2[i - 2]))
#         print("------------------------------------------------------------------------")
#
#
#
#
# a = [1,2,3,4]
#
# print(a.pop(0))
# print(a)


