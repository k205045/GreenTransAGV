from flask import Flask
import app
from threading import Thread
class My_app(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.app = Flask(__name__)
        app.My_flask.register(self.app, route_base='/')


    def run(self):
        self.app.run(debug=False)




if __name__ == '__main__':
    a = My_app()