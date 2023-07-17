# 用于处理vkCode.csv文件,来生成python可读的对象，如果vkCode.py文件出现错误，请运行本脚本重新生成
jtext = {}
with open("./vkCode.csv",mode="r",encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
        data = line.split(",")
        jtext[data[2]] = {"VK_Name":data[0],"VK_Hex":data[1],"VK_CH_Name":data[3]}
    
    with open("./vkCode.py","a+",encoding="utf-8") as exf:
        exf.write("vkDic = " + str(jtext).replace("}, ","},\n"))