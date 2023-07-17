import typing
from PyQt5 import QtCore
from common import appName
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon,QMenu,QAction,QApplication,QWidget

from Ui_about import Ui_Form

class aboutWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.show()
    def close(self):
        super().close()
        
# 托盘
class Tray(QSystemTrayIcon):
    def __init__(self,fatherApp):
        super().__init__()
        self.app = fatherApp
        # 设置托盘图标
        self.setIcon(QIcon("./icon.128px.ico"))

        # 设置托盘菜单
        self.menu = QMenu()

        # 设置菜单的菜单项以及对应的动作
        self.heatMap = QAction("生成热力图",self)
        self.heatMap.triggered.connect(self.heatMapFunc)
        self.menu.addAction(self.heatMap)

        self.outData = QAction("导出统计",self)
        self.outData.triggered.connect(self.outDataFunc)
        self.menu.addAction(self.outData)

        self.menu.addSeparator()

        self.aboutAct = QAction("关于",self) 
        self.aboutAct.triggered.connect(self.aboutActFunc)
        self.menu.addAction(self.aboutAct)

        self.quitAct = QAction("退出",self)
        self.quitAct.triggered.connect(self.quitActFunc)
        self.menu.addAction(self.quitAct)

        self.setContextMenu(self.menu)

        # 设置托盘显示的名称
        self.setToolTip(appName())
        self.setVisible(True)
        self.show()
    def aboutActFunc(self):
        self.abtWindow = aboutWindow()
        
    def quitActFunc(self):
        self.hide()
        self.app.quit()
    def heatMapFunc(self):
        pass
    def outDataFunc(self):
        pass

        

