import os,sys
from common import getTime
from io import TextIOWrapper


class logsFileOprate:
    def __init__(self,fileOpratePointer:TextIOWrapper = None) -> None:
        if(fileOpratePointer is not None):
            self.file = fileOpratePointer
        else:
            # 补全目录
            if(os.path.exists("./logs") == False):
                os.mkdir("./logs")
    def createLogFile(self):
        # 以追加模式打开
        self.file = open("./logs/log-" + str(getTime(2,"YY-MM-DD")) + ".txt",mode="a+",encoding="UTF-8")
    def writeLogs(self,logContent:str) -> int:
        return self.file.write(logContent + "\n")
    def createStartLog(self):
        self.file.write("=====Logs=====\n")
        self.file.write("[info][" + getTime(2,"YY-MM-DD hh:mm:ss") + "] Start Programme\n")
    def close(self):
        self.file.close()
        self.file = None