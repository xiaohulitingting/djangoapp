import logging, os, time, traceback
class LOG:
    def __init__(self, logger):
        self.fileHandlerName = ''
        self.fileHandler = None
        self.loggerName = logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            "=========================\ntime:%(asctime)s \nlogger:%(name)s \nlevel:%(levelname)s \nfile:%(filename)s \nfun:%(funcName)s \nlineno:%(lineno)d \nmessage:%(message)s")
        # 控制台
        '''
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
       '''
        #path = os.path.abspath(os.path.dirname(__file__)) + '/log/' + self.loggerName + '/'
        path = os.path.abspath(os.path.dirname(__file__)) + '/log/'
        #print('log path=', path)

    def setfh(self):
       # fname = time.strftime("%Y%m%d%H")
        fname = time.strftime("%Y%m%d")
        if fname != self.fileHandlerName:
            # 移除原来的句柄
            if self.fileHandler != None:
                self.logger.removeHandler(self.fileHandler)
                # 设置日志文件保存位置
            #path = os.path.abspath(os.path.dirname(__file__)) + '/log/' + self.loggerName + '/'
            path = os.path.abspath(os.path.dirname(__file__)) + '/log/'
            if os.path.isdir(path) == False:
                os.makedirs(path)
            fh = logging.FileHandler(path + fname + '.log')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)

            self.fileHandlerName = fname
            self.fileHandler = fh
            # 格式化日志内容

    def _fmtInfo(self, msg):
        if len(msg) == 0:
            msg = traceback.format_exc()
            return msg
        else:
            _tmp = [msg[0]]
            _tmp.append(traceback.format_exc())
            return '\n**********\n'.join(_tmp)
            # 封装方法

    def debug(self, *msg):
        _info = self._fmtInfo(msg)
        try:
            self.setfh()
            self.logger.debug(_info)
        except:
            print
            'mylog debug:' + _info

    def error(self, *msg):
        _info = self._fmtInfo(msg)
        try:
            self.setfh()
            self.logger.error(_info)
        except:
            print
            'mylog error:' + _info

    def info(self, *msg):
        _info = self._fmtInfo(msg)
        try:
            self.setfh()
            self.logger.error(_info)
        except:
            print
            'mylog info:' + _info

    def warning(self, *msg):
        _info = self._fmtInfo(msg)
        try:
            self.setfh()
            self.logger.error(_info)
        except:
            print
            'mylog warning:' + _info
'''
普通方法,可以通过self访问实例属性
def normalMethod(self,data)
1
类方法,可以通过cls访问类属性
@classmethod
def classMethod(cls,data)
1
2
静态方法,不可以访问,通过传值的方式
@staticmethod
def staticMethod(data)
'''