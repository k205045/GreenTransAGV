from flask import Flask, jsonify, request
from flask_classful import FlaskView
import json
import My_global
import mbservertest
from logger import _logging as log
from time import sleep


k = log()
log = k.Getlogger()
class My_flask(FlaskView):
    default_methods = ['POST']

    def index(self):
    # http://localhost:5000/
        return "<h1>Web Connected!!</h1>"

    # @route('/action')
    def Action(self):#動作執行
        try:
            data = request.data.decode()
            # mbsev = mbservertest.mbclient()
            # print(mbsev.Robotstop())
            # if mbsev.Robotstop() == 0 or mbsev.Robotstop() == None:
            #     res = {
            #         "Result": "N",
            #         "error": 'Unable to run',
            #     }
            #     log.info('Unable to run')
            #     k.Check_Time()
            #     return jsonify(res)
            # else:
            j_data = json.loads(data)
            try:
                res = {
                    "name": "action",
                    "start": j_data["start"],
                    "end": j_data["end"],
                    "location": j_data["location"],
                    "action": j_data["action"],
                    "nolandmark": j_data["nolandmark"],
                    "nobarcode": j_data["nobarcode"]
                }
            except KeyError:
                res = {
                    "name": "action",
                    "start": j_data["start"],
                    "end": j_data["end"],
                    "location": j_data["location"],
                    "action": j_data["action"]
                }
            My_global.set_res(res)
            # print(self.a.Get_res())
            print('APP IN LOOP')
            while True:
                if My_global.get_sen() != None:
                    a = My_global.get_sen()
                    print(a)
                    My_global.set_sen(None)
                    print('APP OUT LOOP')
                    break
                sleep(0.5)

            log.info(a)
            k.Check_Time()
            return jsonify(a)


        except Exception as e:
            # print(data)
            print(e)
            res = {
                "Result":"N",
                "error": e,
            }
            log.info(e)
            k.Check_Time()
            return jsonify(res)



    def Status(self):#狀態詢問
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            b = mbsev.Error_or_Not()
            c = mbsev.Error_code()
            d = mbsev.RobotCompelet()
            e = mbsev.syserrorcode()
            f = mbsev.home()
            g = mbsev.Roboterror()
            h = mbsev.RoboterrorCode()
            i = mbsev.IAI_Error()
            mbsev.conn.close()
            del mbsev
            a = My_global.get_error()
            res = {
                "RobotCompelet": str(d).strip("[]"),
                "Status": str(b).strip("[]"),
                "ErrorCode": str(c).strip("[]"),
                "syserror" : str(a).strip("[]"),
                "Roboterror" : str(g).strip("[]"),
                "RoboterrorCode" : str(h).strip("[]"),
                "home" : str(f).strip("[]")
            }
            # res = {
            #     "RobotCompelet": str(d).strip("[]"),
            #     "Status": str(b).strip("[]"),
            #     "ErrorCode": str(c).strip("[]"),
            #     "syserror": str(a).strip("[]"),
            #     "syserrorCode": str(e).strip("[]"),
            #     "Roboterror": str(g).strip("[]"),
            #     "RoboterrorCode": str(h).strip("[]"),
            #     "home": str(f).strip("[]"),
            #     "IAIerror": str(i).strip("[]")
            # }
            log.info(res)
            k.Check_Time()
            return jsonify(res)

        except Exception as e:
            print(e)
            res = {
                "Result": "N",
                "error": e,
            }
            log.info(e)
            k.Check_Time()
            return jsonify(res)

    def Getbarcode(self):#獲取barcode
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            b = mbsev.GetBarcode()
            mbsev.conn.close()
            del mbsev
            res = {
                "BARCODE": str(b),
            }
            log.info(res)
            k.Check_Time()
            return jsonify(res)

        except Exception as e:
            print(e)
            res = {
                "Result": "N",
                "error": e,
            }
            log.info(e)
            k.Check_Time()
            return jsonify(res)

    def SysErrorReset(self):#本程式異常復歸
        My_global.set_error(None)
        mbsev = mbservertest.mbclient()
        mbsev.ErrorReset()
        res = {
            "Result": "Y",
        }
        # log.info('syserrorreset')
        k.Check_Time()
        return jsonify(res)

    def BufferStatus(self):#Buffer狀態
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            b = mbsev.Get_Sensor()
            mbsev.conn.close()
            del mbsev
            res = {
                "A1": str(b[0]),
                "A2": str(b[3]),
                "B1": str(b[1]),
                "B2": str(b[4]),
                "C1": str(b[2]),
                "C2": str(b[5])
            }
            log.info(res)
            k.Check_Time()
            return jsonify(res)

        except Exception as e:
            print(e)
            res = {
                "Result": "N",
                "error": e,
            }
            log.info(e)
            k.Check_Time()
            return jsonify(res)

    def SetBarcodeCheck(self):#是否獲取barcode
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            mbsev.SetBarcodeCheck(j_data["QRCheck"])
            mbsev.conn.close()
            del mbsev
            res = {
                "Result": "Y",
            }
            log.info(res)
            k.Check_Time()
            return jsonify(res)

        except Exception as e:
            print(e)
            res = {
                "Result": "N",
                "error": e,
            }
            log.info(e)
            k.Check_Time()
            return jsonify(res)



if __name__ == '__main__':
    app123 = Flask(__name__)
    My_flask.register(app123, route_base='/')
    app123.run(debug=True)