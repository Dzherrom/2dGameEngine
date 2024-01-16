import time as time
from datetime import datetime

class Logger:
    def __init__(self):
        self.lo = []
        self.now = datetime.now()
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def log(self, message):
        
        print("\033[32m[%s] LOG: %s\033[0m" % (self.timestamp, message))
    
    def err(self, message):
         print("\033[31m[%s] ERROR: %s\033[0m" % (self.timestamp, message))
