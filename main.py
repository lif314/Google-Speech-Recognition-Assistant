import os
import sys
from threading import Thread

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon


from addView import AddView
from mainView import MainView
from asr import Asr
from executeCmds import ExecuteCmds
from cmdAppDatabase import get_as_dic
from musicView import Music

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
        self.musicMedia = Music()

        self.addView.ui.returnButton.clicked.connect(self.to_main)
        self.mainView.ui.addButton.clicked.connect(self.to_add)
        self.mainView.ui.mediaButton.clicked.connect(self.to_musicMedia)
        # self.mainView.ui.listenButton.clicked.connect(self.listen)


    def to_main(self):
        self.addView.ui.close()
        self.mainView.ui.show()

    def to_add(self):
        self.addView.ui.show()

    def to_musicMedia(self):
        # TODO 子界面向主界面传入参数
        # self.mainView.ui.musicTextEdit.setPlainText(self.musicMedia.cursong)
        self.musicMedia.show()
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
        print("界面处理失败!")

    # 获取app cmds
    dic = get_as_dic()
    cmds = dic.keys()
    # 命令执行器
    cmdExecutor = ExecuteCmds()
    while True:
        res = asr.recognizeByGoogle()
        # TODO 实时显语音识别响应结果 respTextEdit
        # view.mainView.ui.respTextEdit.setPlainText("识别结果：" + res)
        print("识别结果：", res)
        res = res.lower()
        if res.find("stop") >= 0:
            os._exit(0)
            # sys.exit(1)
        elif res.find("music") >= 0:
            # 新建一个线程进行处理
            music_thread = Thread(target=cmdExecutor.play_music)
            music_thread.start()
            continue
            # cmdExecutor.play_music()
        elif res in cmds:
            for cmd in cmds:
                if(res == cmd):
                    open_thread = Thread(target=cmdExecutor.open_app(dic.get(cmd)))
                    open_thread.start()
                    break
        else:
            continue