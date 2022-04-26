import speech_recognition as sr


"""
语音识别模块：
    - 获取Audio
    - speech recognition识别语音
    - 打开程序运行文件
"""

class Asr:
    def __init__(self):
        self.dic = {}
        self.keys = []

    # obtain audio from the microphone
    def getAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
            return r, r.listen(source)


    # recognize speech using Google Speech Recognition
    # 这个效果不错，只是延迟比较严重
    def recognizeByGoogle(self):
        r, audio = self.getAudio()
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            res = r.recognize_google(audio)
            # print("Google Speech Recognition thinks you said " + res)
            return res
            # if(res == 'play music'):
            #     playsound("./music/qingtian.mp3")
            # else:
            #     self.dic = get_as_dic()
            #     self.keys = self.dic.keys()
            #     for key in self.keys:
            #         if(res == key):
            #             path = self.dic.get(key)
            #             self.open_app(path)
            #             break
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)


if __name__ == '__main__':
    asr  = Asr()
    asr.recognizeByGoogle()