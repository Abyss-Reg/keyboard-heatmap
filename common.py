import time

app_name = "keyboard heatmap"


def appName():
    return app_name


def getTime(timeMode:int,timeFormat:str = None):
    '''
        参数：
            timeMode:int 取时间的形式，取值范围0到2
            timeFormat:str 时间格式，当timeMode为2时生效
                timeFormat中允许使用的占位符如下
                    YY 表示年份
                    MM 表示月份
                    DD 表示日期
                    hh 表示小时(24小时制)
                    mm 表示分钟
                    ss 表示秒钟
        返回：
            指定的时间
    '''
    ret = str()
    if(timeMode == 0):
        # timeMode 0 毫秒级时间戳
        ret = int(time.time() * 1000)
    elif(timeMode == 1):
        # timeMode 1 秒级时间戳
        ret =  int(time.time())
    elif(timeMode == 2):
        # timeMode 2 格式化时间
        t = time.localtime()
        # 解析时间格式
        # YY-MM-DD hh:mm:ss
        if(timeFormat == "" or timeFormat == None):
            class FormatError(Exception):
                def __init__(self, *args: object) -> None:
                    super().__init__(*args)
            raise FormatError("timeFormat cannot be None when timeMode is 2")
        else:
            s = timeFormat.replace("YY",str(t[0])).replace("MM",str(t[1] if t[1]>=10 else "0" + str(t[1]))).replace("DD",str(t[2] if t[2]>=10 else "0"+str(t[2]))).replace("hh",str(t[3] if t[3]>=10 else "0"+str(t[3])))
            s = s.replace("mm",str(t[4] if t[4]>=10 else "0"+str(t[4]))).replace("ss",str(t[5] if t[5]>=10 else "0"+str(t[5])))
            ret = s
    else:
        class InputError(Exception):
            def __init__(self, *args: object) -> None:
                super().__init__(*args)   
        raise InputError("timeMode must between 0 and 2")
    return ret