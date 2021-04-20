from flask import Flask, jsonify, request
from flask_classful import FlaskView, route
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
    def Action(self):
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            res = {
                "name": "action",
                "start": j_data["start"],
                "end": j_data["end"],
                "location": j_data["location"],
                "action": j_data["action"],
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



    def Status(self):
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            b = mbsev.Error_or_Not()
            c = mbsev.Error_code()
            d = mbsev.RobotCompelet()
            mbsev.conn.close()
            del mbsev
            a = My_global.get_error()
            res = {
                "RobotCompelet": str(d).strip("[]"),
                "Status": str(b).strip("[]"),
                "ErrorCode": str(c).strip("[]"),
                "syserror":str(a)
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

    def Getbarcode(self):
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

    def SysErrorReset(self):
        My_global.set_error(None)
        res = {
            "Result": "Y",
        }
        # log.info('syserrorreset')
        k.Check_Time()
        return jsonify(res)

    def errorHandling(self):
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            a = My_global.get_error()
            res = {
                "Result": "Y",
                "Status": a,
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

    def BufferStatus(self):
        try:
            data = request.data.decode()
            j_data = json.loads(data)
            mbsev = mbservertest.mbclient()
            b = mbsev.Get_Sensor()
            mbsev.conn.close()
            del mbsev
            res = {
                "A1": str(b[3]),
                "A2": str(b[0]),
                "B1": str(b[4]),
                "B2": str(b[1]),
                "C1": str(b[5]),
                "C2": str(b[2])
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

    def SetBarcodeCheck(self):
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