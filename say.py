import os
try:
    os.system('pip install SpeechRecognition')
except:
    print('please install this Library \003[1;31mpip install SpeechRecognition')
import speech_recognition as sr #pip install SpeechRecognition
r = sr.Recognizer()
micro = sr.Microphone(device_index=1)
with sr.Microphone() as source:
    print('say something...')
    audio = r.listen(source)
text = r.recognize_google(audio)
print(text)
