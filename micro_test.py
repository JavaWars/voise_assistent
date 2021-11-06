import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    print('Слушаю вас ... ')
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("Вы сказали "+query.lower())
