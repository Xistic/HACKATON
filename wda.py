import pyttsx3 
import speech_recognition as sr

r = sr.Recognizer()

engine = pyttsx3.init()

words=''
while words != "пока":
    with sr.Microphone()as source:
        audio=r.listen(source)
        words=r.recognize_google(audio,language='Ru-ru').lower()
        engine.say(words)
        engine.runAndWait()


#__________________ПРЕОБРАЗОВАНИЕ РЕЧИ В "ТЕХНО" голос. Дополнив код библиотекой pyttsx3__________________

