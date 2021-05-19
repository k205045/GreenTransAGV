import logging
import os
from logging import handlers
import time
#log管理
class _logging():
    def Getlogger(self,filename = 'default.log'):
        level = logging.INFO
        # filename = 'default.log'
        datefmt = '%Y-%m-%d %H:%M:%S'
        format = '%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'

        self.log = logging.getLogger(filename)
        format_str = logging.Formatter(format, datefmt)

        def namer(filename):
            return filename.split('default.')[1]

        self.cmd = logging.StreamHandler()
        self.cmd.setFormatter(format_str)
        self.cmd.setLevel(level)

        format_str = logging.Formatter(format, datefmt)
        # os.makedirs("./debug/logs", exist_ok=True)
        os.makedirs('./logs', exist_ok=True)
        log_path = os.getcwd() + "/logs/"
        self.log_time = time.strftime("%Y-%m-%d")
        filename = log_path + self.log_time + '.log'

        # th_debug = handlers.TimedRotatingFileHandler(filename="./debug/" + filename, when='S',
        #                                              encoding='utf-8')
        # # th_debug.namer = namer
        # # th_debug.suffix = "%Y-%m-%d%.log"
        # th_debug.setFormatter(format_str)
        # th_debug.setLevel(logging.DEBUG)
        # log.addHandler(th_debug)

        self.th = logging.FileHandler(filename, 'a', encoding='utf-8')
        # th.namer = namer
        # th.suffix = "%Y-%m-%d_%H-%M.log"
        self.th.setFormatter(format_str)
        self.th.setLevel(logging.INFO)
        self.log.addHandler(self.th)
        self.log.addHandler(self.cmd)
        self.log.setLevel(level)
        return self.log

    def Check_Time(self):
        log_time = time.strftime("%Y-%m-%d")
        if self.log_time != log_time:
            self.log.removeHandler(self.th)
            self.log.removeHandler(self.cmd)
            return self.Getlogger()
        return self.log

    def Del_logging(self):
        self.log.removeHandler(self.th)
        self.log.removeHandler(self.cmd)


# logger = _logging()

if __name__ == '__main__':

    logger,hdlr = _logging().Getlogger()
    for i in range(3):
        time.sleep(1)
        logger.info('HIHIHI')
    for i in hdlr:
        logger.removeHandler(i)
    logger,hdlr = _logging().Getlogger()
    for i in range(3):
        time.sleep(1)

        logger.info('HIHIHI')
