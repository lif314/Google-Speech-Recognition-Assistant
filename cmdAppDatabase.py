import os

"""
文本数据库：
    存储语音命令与对应的软件路径
    eg:
    open notepad:D:\\AppData\\Notepad++\\notepad++.exe
"""

# 命令-应用程序路径 文本数据库

# 添加数据
def add_to_file(cmd, path):
    print(cmd, path)
    if cmd is '' or path is '':
        print("路径选择为空！")
    else:
        f = open(r'./textDatabase/cmd_app.text', 'a', encoding='UTF-8')
        f.write(cmd + '->' + path + '\n')
        f.close()

# 获取命令数据
def get_as_dic() -> dict:
    # cmd_apppath 键值对
    dic = {}
    fr = open(r'./textDatabase/cmd_app.text', 'r', encoding='UTF-8')
    for line in fr:
        value = line.strip().split('->')
        dic[value[0]] = value[1]
    fr.close()
    return dic


# 打开应用程序
def open_app(app_dir):
    os.startfile(app_dir)



if __name__ == '__main__':
    dic = get_as_dic()
    print(dic.keys())
    # cmd = "open tts"
    # path = "D:\AppData\Anaconda\envs\pyqt\Lib\site-packages\PySide2\designer.exe"
    # add_to_file(cmd, path)
    # 打开应用程序
    for cmd, path in dic.items():
        open_app(path)
    # print(dic)