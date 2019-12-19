"""
经济词典中所使用的通用函数。包括：

errlog：错误日志
getdic：从github上下载已经整理好的数据文件
"""

def errlog(message):
    """
    写入错误日志到logfile.txt
    需要的输入：错误信息message
    """
    import os
    import time
    with open(os.path.dirname(os.path.realpath(__file__))+"/logfile.txt",'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S  ",time.localtime())+message+'\n')

def getdic(filename):
    """
    从GitHub上下载已经整理好的词典文件。
    需要的输入：文件名filename
    """
    import os
    import requests
    import sys
    url="https://raw.githubusercontent.com/sijichun/jingjidic/master/sub_dics/"+filename
    PWD=os.path.dirname(os.path.realpath(__file__))
    try:
        html=requests.get(url).text
        with open(PWD+'/sub_dics/'+filename,'w') as f:
            f.write(html)
    except Exception as e:
        print("错误："+str(e))
        sys.exit(1)