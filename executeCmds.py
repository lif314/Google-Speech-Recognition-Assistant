import os

from playsound import playsound

"""
语音命令执行
"""

class ExecuteCmds:
    # 打开应用程序
    def open_app(self, app_dir):
        os.startfile(app_dir)

    # 播放音乐
    def play_music(self):
        playsound("./music/qingtian.mp3")

if __name__ == '__main__':
    a = ExecuteCmds()
    a.play_music()