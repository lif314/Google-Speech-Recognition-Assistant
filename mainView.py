from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtUiTools import QUiLoader

from cmdAppDatabase import get_as_dic


class MainView:
    def __init__(self):
        self.ui = QUiLoader().load("ui/main.ui")

        self.ui.searchButton.clicked.connect(self.search_cmds)
        self.ui.musicButton.clicked.connect(self.search_music)

    # 查询打开程序的语音命令列表
    def search_cmds(self):
        dic = get_as_dic()
        keys = dic.keys()
        str = ""
        for key in keys:
            str = str + key + "\n"
        self.ui.cmdTextEdit.setPlainText(str)

    # 查询音乐播放列表
    def search_music(self):
        self.ui.musicTextEdit.setPlainText("晴天.mp3")
        # print("查询音乐播放列表")
