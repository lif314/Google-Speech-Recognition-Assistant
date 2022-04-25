from PyQt5 import QtWidgets, QtGui, QtCore, uic

from playsound import playsound
from asrInterface import Ui_MainWindow
import sys

import os

import speech_recognition as sr

from CmdAppDatabase import get_as_dic


# obtain audio from the microphone
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        return r, r.listen(source)

# 打开应用程序
def open_app(app_dir):
    os.startfile(app_dir)

dic = get_as_dic()
cmds = dic.keys()
# recognize speech using Google Speech Recognition
# 这个效果不错，只是延迟比较严重
def recognizeByGoogle():
    r, audio = getAudio()
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        res = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + res)

        if(res == 'play music'):
            playsound("./music/qingtian.mp3")
        else:
            for key in cmds:
                if(res == key):
                    path = dic.get(key)
                    open_app(path)
                    break
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = ""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    # 监听
    recognizeByGoogle()
    sys.exit(app.exec())