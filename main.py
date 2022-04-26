import sys
from threading import Thread

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon


from addView import AddView
from mainView import MainView
from asr import Asr
from executeCmds import ExecuteCmds
from cmdAppDatabase import get_as_dic

"""
主程序
    - 打开应用程序
    - 播放音乐
"""

asr = Asr()

# 系统路由处理
class AsrView:
    def __init__(self):
        self.addView = AddView()
        self.mainView = MainView()

        self.addView.ui.returnButton.clicked.connect(self.to_main)
        self.mainView.ui.addButton.clicked.connect(self.to_add)
        # self.mainView.ui.listenButton.clicked.connect(self.listen)


    def to_main(self):
        self.addView.ui.close()
        self.mainView.ui.show()

    def to_add(self):
        self.addView.ui.show()

    # def listen(self):
    #     # 子线程监听用户语音: 如果采用循环，会导致线程爆炸
    #     thread = Thread(target=asr.recognizeByGoogle)
    #     thread.start()


def start_view():
    app = QApplication([])
    # 设置主窗口图标
    app.setWindowIcon(QIcon("./icon/phone.png"))
    view = AsrView()
    view.mainView.ui.show()
    app.exec_()


if __name__ == '__main__':
    view_thread = Thread(target=start_view)
    # 语音监听
    thread = Thread(target=asr.recognizeByGoogle)
    try:
        view_thread.start()
    except:
        print("界面处理失败")

    # 获取app cmds
    dic = get_as_dic()
    cmds = dic.keys()
    # 命令执行器
    cmdExecutor = ExecuteCmds()
    while True:
        res = asr.recognizeByGoogle()
        print("识别结果：", res)
        if res.find("quit"):
            sys.exit(0)

        if res.find("music"):
            cmdExecutor.play_music()
        else:
            for cmd in cmds:
                if(res == cmd):
                    cmdExecutor.open_app(dic.get(cmd))
