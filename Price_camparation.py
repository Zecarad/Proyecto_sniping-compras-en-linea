

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()  #inicio de motor
engine.setProperty('rate', 200)  #sonfiguracion de voz
engine.setProperty('voice', 'spanish')

r= sr.Recognizer()



def speak(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    with sr.Microphone as source:   #habilita el micorofono
        print("Ahora es el momento de hablar")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es-ES")
            print("He comprendido: {}".format(text))
            return text
        except sr.UnknownValueError:
            return



if __name__ =="__main__":
    speak("Pueba si funciona")
    print(listen())



