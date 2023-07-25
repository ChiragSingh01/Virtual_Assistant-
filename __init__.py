import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import cv2
import mediapipe as mp
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Function to speak the given command in Audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function to greet the master
def wishme(master):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning {master}")

    elif 12 <= hour < 18:
        speak(f"Good Afternoon {master}")

    elif 18 <= hour < 21:
        speak(f"Good Evening {master}")

    else:
        speak(f"Good Night {master}")


def awake():
    r = sr.Recognizer()
    with sr.Microphone() as Mic:
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(Mic)

    try:
        query = r.recognize_google(audio, language='en-in')
        return query


    except Exception as e:
        pass


# Listen the input using microphone and output as a string
def take_command():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as Mic:
            speak("listening")
            r.pause_threshold = 1
            r.energy_threshold = 1000
            audio = r.listen(Mic)

        try:
            speak("recognizing")
            query = r.recognize_google(audio, language='en-in')
            return query


        except Exception as e:
            speak("say that again please")


# function to search on wikipedia
def search_wikipedia(query):
    speak("searching wikipedia")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=3)
    print(result)
    speak(f"According to wikipedia {result}")


# function to open somthing from browser
def open_browser(query):
    query = query.replace("open ", "")
    print(f"{query}.com")
    webbrowser.open(f"{query}.com")


# function to search on YouTube
def searchyt(query):
    speak("getting that from youtube")
    query = query.replace(" song", "")
    query = query.replace("play ", "")
    query = query.replace(" on youtube", "")
    pywhatkit.playonyt(query)


# function to send mail
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chiragsingh93135@gmail.com', 'password')
    server.sendmail('chiragsingh93135@gmail.com', to, content)
    server.close()
