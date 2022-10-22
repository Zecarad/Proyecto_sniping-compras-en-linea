import pyttsx3
import speech_recognition as sr
import re

from pyttsx3 import engine


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", "120")
    engine.setProperty("voice", "spanish")
    return engine

def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text


def reading(text):
    name = None
    patterns = ["Me llamo ([A-Za-z])"]
    for patterns in patterns:
        try:
            name = re.findall(patterns, text)[0]
        except IndexError:
            pass
        return name



def main():
    engine = initialize_engine()
    engine.say("Hola, que tal ?")
    engine.runAndWait()


    r = sr.Recognizer()

    text = recognize_voice(r)
    name = reading(text)
    if name:
        engine.say("Encantado de conocerte {}".format(name))
    else:
        engine.say("No se ha entendido el mensaje")
    engine.runAndWait()


if __name__ =="__main__":
    main()

