from logs import logsFileOprate
from ui import Tray
from PyQt5.QtWidgets import QApplication
from hook import keyboardHook

# 程序入口
if __name__ == '__main__':
    # 打开或者新建日志文件
    log = logsFileOprate()
    log.createLogFile()
    log.createStartLog()
    # 载入托盘
    app = QApplication([])
    tray = Tray(app)
    class selfHook(keyboardHook):
        def __init__(self, fileOpratePointer=None) -> None:
            super().__init__(fileOpratePointer)
        
        def selfHookProc(self, nCode, wParam, kbStruct):
            if(nCode == 0):
                if(wParam != 260):
                    ...
    

    app.exec_()