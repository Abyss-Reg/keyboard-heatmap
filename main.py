from logs import logsFileOprate

# 程序入口
if __name__ == '__main__':
    # 打开或者新建日志文件
    log = logsFileOprate()
    log.createLogFile()
    log.createStartLog()
    