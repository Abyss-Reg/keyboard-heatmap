# 代码参考自https://zhuanlan.zhihu.com/p/166359660
import sys
from ctypes import *
from ctypes.wintypes import DWORD, HHOOK, HINSTANCE, MSG, WPARAM, LPARAM
from logs import logsFileOprate
from common import getTime

user32 = CDLL("user32.dll")
kernel32 = CDLL("kernel32.dll")

class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode', DWORD),
        ('scanCode', DWORD),
        ('flags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', DWORD)]

def uninstallHookProc(hooked):
    if hooked is None:
        return
    user32.UnhookWindowsHookEx(hooked)
    hooked = None

def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg), 0, 0, 0)

def installHookProc(hooked, pointer):
    hooked = user32.SetWindowsHookExA(
        13,
        pointer,
        kernel32.GetModuleHandleW(),
        0
    )
    if not hooked:
        return False
    return True

HOOKPROC = WINFUNCTYPE(c_int, c_int, c_int, POINTER(DWORD))
hooked = None

class keyboardHook():
    def __init__(self,fileOpratePointer = None) -> None:
        self.fileOpratePointer = fileOpratePointer

    def init_hook(self):
        pointer = HOOKPROC(self.hookProc)
        self.logFile = logsFileOprate(self.fileOpratePointer)
        if installHookProc(hooked, pointer):
            self.logFile.writeLogs("[info]["+getTime(2,"YY-MM-DD hh:mm:ss")+"] Keyboard Hook Installed Succeed")
            msg = MSG()
            user32.GetMessageA(byref(msg), 0, 0, 0)
            
        else:
            self.logFile.writeLogs("[error]["+getTime(2,"YY-MM-DD hh:mm:ss")+"] Keyboard Hook Installed Failed")
            ...

    def hookProc(self,nCode, wParam, lParam):
        self.selfHookProc(nCode,wParam,cast(lParam, POINTER(KBDLLHOOKSTRUCT)).contents)    
        return user32.CallNextHookEx(hooked, nCode, wParam, lParam)

    def uninstall(self):
        uninstallHookProc(hooked)
        # self.logFile.writeLogs("[info]["+getTime(2,"YY-MM-DD hh:mm:ss")+"] Keyboard Hook Uninstalled")

    def selfHookProc(self, nCode, wParam, kbStruct):
        # 这里是按键的业务逻辑
        print(kbStruct.vkCode,kbStruct.flags,wParam)


