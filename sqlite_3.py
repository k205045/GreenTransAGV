import sqlite3
from pprint import pprint
from decimal import Decimal, ROUND_HALF_UP
from logger import _logging as log



class My_sqlite():
    def __init__(mysqlite):
        mysqlite.conn = sqlite3.connect('TM.db')  # Sqlite

    def Ins_TM(mysqlite, result):
        if mysqlite.Get_TM(result[0]) == []:
            mysqlite.conn.execute("""INSERT INTO TMoffset(local ,M0 ,offset1 ,offset2 ,offset3 ,offset4 ,offset5 ,offset6)  VALUES (
                                ?,?,?,?,?,?,?,?);""", tuple(result))
            mysqlite.conn.commit()
        else:
            mysqlite.Upd_TM(result[0], result)

    def Upd_TM(mysqlite, local, result):
        # for i in range(len(result)):
        #     result[i] = result[i].strip(',')

        mysqlite.conn.execute("""UPDATE TMoffset SET
                            local = ?,
                            M0 = ?,
                            offset1 = ?,
                            offset2 = ?,
                            offset3 = ?,
                            offset4 = ?,
                            offset5 = ?,
                            offset6 = ?

                            WHERE local = '""" + local + """' ;""", tuple(result))

        mysqlite.conn.commit()

    def Del_TM(mysqlite, local):
        mysqlite.conn.execute("DELETE from TMoffset where local='" + local + "';")
        mysqlite.conn.commit()

    def Get_TM(mysqlite, local):
        cursor = mysqlite.conn.execute(
            """SELECT  local ,M0 ,offset1, offset2, offset3 ,offset4 ,offset5 ,offset6
             FROM TMoffset  WHERE  local Like '""" + local + """';""")
        mysqlite.conn.commit()
        if cursor:
            return [list(x) for x in cursor]
        return False

    def Get_TM_all(mysqlite, local):
        cursor = mysqlite.conn.execute(
            """SELECT  M0, offset1, offset2, offset3 ,offset4 ,offset5 ,offset6
             FROM TMoffset  WHERE  local Like '""" + local + """';""")
        mysqlite.conn.commit()
        if cursor:
            return [list(x) for x in cursor]
        return False

    def Get_ALL(mysqlite):
        cursor = mysqlite.conn.execute(
            """SELECT  local ,offset1, offset2, offset3 ,offset4 ,offset5 ,offset6
             FROM TMoffset ;""")
        mysqlite.conn.commit()
        if cursor:
            return [list(x) for x in cursor]
        return False

    def Average(mysqlite, lst):
        return sum(lst) / len(lst)


if __name__ == '__main__':
    mysqlite = My_sqlite()
    k = log()
    log = k.Getlogger("TM.log")
    #     mysqlite.conn.execute("""
    #     CREATE TABLE "TMoffset" (
    # 	"local"	TEXT,
    # 	"offset1"	TEXT,
    # 	"offset2"	TEXT,
    # 	"offset3"	TEXT,
    # 	"offset4"	TEXT,
    # 	"offset5"	TEXT,
    # 	"offset6"	TEXT
    # );""")
    #     mysqlite.conn.commit()
    #     mysqlite.Ins_TM(['E1-1-1-4', '243.34, -124.2, 0.87, 0.59, -0.37, 9.13', '32.72, 272.67, -1.57, -0.41, 0.8, -8.23', '-17.1, 201.97, -0.21, -0.07, 0.38, -0.71', '', '', ''])
    #     plog.info(mysqlite.Get_TM_all("EQ999-1-A1-A2-A3"))
    c = [-1147.06, 17.44, 48.87, -179.65, -0.08, 87.23]
    d = ["EQ999-1-A1-A2-A3", -1142.68, 2.88, 49.63, -179.69, -0.08, 88.74]
    M1 = mysqlite.Get_TM(d[0])[0][2]
    M0 = mysqlite.Get_TM(d[0])[0][1]
    G_Master = mysqlite.Get_TM_all("G_MASTER")[0]
    for i in range(4):
        G_Master.pop(3)
    print(G_Master)
    L_Master = mysqlite.Get_TM_all("L_MASTER")[0]
    if M1:
        M1 = M1.split(",")
        M0 = M0.split(",")
        _G_Master = ["", "", ""]
        _G_Master[0] = G_Master[0].split(",")
        _G_Master[1] = G_Master[1].split(",")
        _G_Master[2] = G_Master[2].split(",")
        _L_Master = ["", "", ""]
        _L_Master[0] = L_Master[0].split(",")
        _L_Master[1] = L_Master[1].split(",")
        _L_Master[2] = L_Master[2].split(",")

        # data = str([float(Decimal(c[i]) - Decimal(d[i])) for i in range(0, len(d))]).\
        #     replace("[", "{").replace("]", "}")

        tmp_z = []
        tmp_x = []
        tmp_y = []
        for i in range(0, 3):
            tmp_z.append(-Decimal(_G_Master[i][5]) + Decimal(_L_Master[i][5]))
            tmp_x.append(-Decimal(_G_Master[i][0]) + Decimal(_L_Master[i][0]))
            tmp_y.append(-Decimal(_G_Master[i][1]) + Decimal(_L_Master[i][1]))
        tmp_z = mysqlite.Average(tmp_z)
        tmp_x = mysqlite.Average(tmp_x)
        tmp_y = mysqlite.Average(tmp_y)
        # log.info(tmp)
        log.info(M0)
        log.info("a" +str(c))

        angle = Decimal(c[5]) - (Decimal(M0[5]) - Decimal(tmp_z))
        from math import cos, sin, pi

        a = (Decimal(M1[0]) - Decimal(M0[0]))
        b = (Decimal(M1[1]) - Decimal(M0[1]))

        x = Decimal(M1[0]) * Decimal(cos(angle * Decimal(pi) / 180)) + Decimal(M1[1]) * \
            Decimal(sin(angle * Decimal(pi) / 180)) - (Decimal(M1[0]) - Decimal(M0[0])) - tmp_x
        y = Decimal(M1[1]) * Decimal(cos(angle * Decimal(pi) / 180)) - Decimal(M1[0]) * \
            Decimal(sin(angle * Decimal(pi) / 180)) - (Decimal(M1[1]) - Decimal(M0[1])) - tmp_y

        log.info("x="+ str(float(x.quantize(Decimal('.00'), ROUND_HALF_UP))))
        log.info("y="+ str(float(y.quantize(Decimal('.00'), ROUND_HALF_UP))))
        # x = -1074.87
        # y = -186.75