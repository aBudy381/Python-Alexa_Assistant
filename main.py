import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from translate import Translator

r = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 120)  # Speed percent (can go over 100)
engine.setProperty('volume', 1.2)  # Volume 0-
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(speech):
    engine.say(speech)
    engine.runAndWait()


with sr.Microphone() as source:
    print('Say something...')
    audio = r.listen(source)


def command():
    try:
        text = r.recognize_google(audio)
        text = text.lower()
        if 'alexa' in text:
            print(text)
    except:
        pass
    return text


def order():
    text = r.recognize_google(audio)
    text = text.lower()
    if 'alexa' in text:
        txt = text.replace('alexa say', '')
        print(txt)
        talk(txt)


def run_alexa():
    text = command()
    if 'play' in text:
        song = text.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'say' in text:
        order()
    elif 'time' in text:
        date = datetime.datetime.now().strftime('%I:%M %p')
        print(date)
        talk('the time is' + date)
    elif "who is" in text:
        person = text.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    # elif 'translate' in text:
    else:
        talk("i didn't understand you, please say it again.")


while True:
    run_alexa()
