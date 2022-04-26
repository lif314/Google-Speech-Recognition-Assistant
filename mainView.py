from threading import Thread

from PySide2.QtUiTools import QUiLoader
from PySide2.QtMultimedia import QMediaPlayer

from cmdAppDatabase import get_as_dic
from cloudMusic import NeteaseCloudMusicApi


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
        def threadFunc():
            musicApi = NeteaseCloudMusicApi()
            songs = musicApi.get_new_songs_details()
            names = ""
            for song in songs:
                names = names + song['name'] + "\n"
            self.ui.musicTextEdit.setPlainText(names)
        music_thread = Thread(target=threadFunc)
        music_thread.start()

        # print("查询音乐播放列表")
