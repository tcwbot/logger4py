import os

### pylogger
# TODO
# done - append to log file.
# done - rolling files.
# done - max_filesize
# done - max number of files.
# - add Configuration Method to consume cfg file. config.dictObj(params)
# - add documentation
# - use bitshift for max_filesize=(1 << 30)
# - create a enum class for levels, instead class vars.
# - FR: Add micro-millisecs options
# https://stackoverflow.com/questions/25017658/microsecond-accurate-timestamp-in-python
###   

class Logger:
    ERROR=0;INFO=1;WARN=2;DEBUG=3;
    def __init__(self):
        self.level=1
        self.suffix='default'
        self.max_no_files=10
        self.max_filesize=1000000
    def check_filesize(self):
        try:
            filesize=os.stat(self.suffix+'.log').st_size
            if (filesize >= self.max_filesize):
                iter_list=list(range(self.max_no_files))
                for i in iter_list[:0:-1]:
                    if os.path.isfile(self.suffix+'.log.'+str(i)) and os.path.isfile(self.suffix+'.log'):
                        os.rename(self.suffix+'.log.'+str(i),self.suffix+'.log.'+str(i+1))
                os.rename(self.suffix+'.log',self.suffix+'.log.1')
        except Exception as e:
            wlog=f'[{time.strftime("%m-%d-%Y %H:%M:%S %p %Z")}] [critical] {e}'
            with open(self.suffix+'.log', "a+") as file:
                file.writelines(wlog+'\n')
    def set_log_level(self,level):
        self.level=level
    def set_log_suffix(self,suffix):
        self.suffix=suffix
    def error(self,msg):
        self.check_filesize()
        if self.level >= self.ERROR:
            self.write_log('error',self.suffix,msg)
    def info(self,msg):
        self.check_filesize()
        if self.level >= self.INFO:
            self.write_log('info',self.suffix,msg)
    def warn(self,msg):
        self.check_filesize()
        if self.level >= self.WARN:
            self.write_log('warn',self.suffix,msg)
    def debug(self,msg):
        self.check_filesize()
        if self.level >= self.DEBUG:
            self.write_log('debug',self.suffix,msg)
    @staticmethod
    def print_log(loglevel,suffix,msg):
        print(f'[{time.strftime("%m-%d-%Y %H:%M:%S %p %Z")}] [{loglevel}] {msg}')
    @staticmethod
    def write_log(loglevel,suffix,msg):
        try:
            wlog=f'[{time.strftime("%m-%d-%Y %H:%M:%S %p %Z")}] [{loglevel}] {msg}'
            with open(suffix+'.log', "a+") as file:
                file.writelines(wlog+'\n')
        except Exception as e:
            wlog=f'[{time.strftime("%m-%d-%Y %H:%M:%S %p %Z")}] [critical] {e}'
            with open(suffix+'.log', "a+") as file:
                file.writelines(wlog+'\n')
    
    
    
