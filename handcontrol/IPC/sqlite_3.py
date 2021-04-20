import sqlite3


class My_sqlite():
    def __init__(self):
        self.conn = sqlite3.connect('TM.db')  # Sqlite

    def Ins_TM(self, result):
        print(result)
        if self.Get_TM(result[0]) == []:
            self.conn.execute("""INSERT INTO TMoffset(local ,offset1 ,offset2 ,offset3 ,offset4 ,offset5 ,offset6)  VALUES (
                                ?,?,?,?,?,?,?);""", tuple(result))
            self.conn.commit()
        else:
            self.Upd_TM(result[0],result)

    def Upd_TM(self, local, result):
        # for i in range(len(result)):
        #     result[i] = result[i].strip(',')

        self.conn.execute("""UPDATE TMoffset SET
                            local = ?,
                            offset1 = ?,
                            offset2 = ?,
                            offset3 = ?,
                            offset4 = ?,
                            offset5 = ?,
                            offset6 = ?
                            
                            WHERE local = '""" + local + """' ;""", tuple(result))

        self.conn.commit()

    def Del_TM(self, local):
        self.conn.execute("DELETE from TMoffset where local='" + local + "';")
        self.conn.commit()

    def Get_TM(self, local):
        cursor = self.conn.execute(
            """SELECT  local ,offset1, offset2, offset3 ,offset4 ,offset5 ,offset6
             FROM TMoffset  WHERE  local Like '""" + local + """';""")
        self.conn.commit()
        if cursor:
            return [list(x) for x in cursor]
        return False


if __name__ == '__main__':
    mysqlite = My_sqlite()
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
    print(mysqlite.Get_TM("E1-1-1-4"))


