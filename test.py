import speech_recognition as sr

r = sr.Recognizer()



words=''
while words != "пока":
	with sr.Microphone()as source:
		audio=r.listen(source)
		words=r.recognize_google(audio,language='Ru-ru').lower()
		print (words)


input()

#__________________ПРЕОБРАЗОВАНИЕ РЕЧИ В ТЕКС__________________



















input()
