
import speech_recognition as sr
import time
import os
from playsound import playsound

# # Working with audio files
# r = sr.Recognizer()
# speech = sr.AudioFile('f1lcapae.wav')
# with speech as source:
#     audio = r.record(source)
# print(r.recognize_sphinx(audio))
#
# # Working with Microphones
# mic = sr.Microphone()
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# r.recognize_sphinx(audio)

# microphone_recognition


# program dir
notepad_dir = r'D:\AppData\Notepad++\notepad++.exe'


# obtain audio from the microphone
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        return r, r.listen(source)

# recognize speech using Sphinx
# 这个效果是个渣渣
def recognizeBySphinx():
    r, audio = getAudio()
    try:
        print('Sphinx thinks you said ' + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


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
        if(res == 'hello'):
            playsound("./music/qingtian.mp3")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def recognizeByGoogleCloud():
    r, audio = getAudio()
    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    try:
        print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio,
                                                                                credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


# 打开应用程序
def open_app(app_dir):
    os.startfile(app_dir)


if __name__ == "__main__":
    start = time.time()
    recognizeByGoogle()
    # open_app(notepad_dir)
    end = time.time()
    print("Time = ", end - start)