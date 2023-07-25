import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# Function to speak the given command in Audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to greet the master
def WishMe(Master):
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak(f"Good Morning {Master}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {Master}")

    elif hour >=18 and hour < 21:
        speak(f"Good Evening {Master}")

    else:
        speak(f"Good Night {Master}")

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
def TakeCommand():
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as Mic:
            speak("listening")
            r.pause_threshold = 1
            r.energy_threshold=1000
            audio = r.listen(Mic)

        try:
            speak("recognizing")
            query = r.recognize_google(audio, language='en-in')
            return query


        except Exception as e:
            speak("say that again please")

# function to search on wikipedia
def SearchWikipedia(query):
    speak("searching wikipedia")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=3)
    print(result)
    speak(f"According to wikipedia {result}")

# function to open somthing from browser
def open(query):
    query = query.replace("open ", "")
    print(f"{query}.com")
    webbrowser.open(f"{query}.com")

# function to search on youtube
def SearchYT(query):
    speak("getting that from youtube")
    query = query.replace(" song", "")
    query = query.replace("play ", "")
    query = query.replace (" on youtube", "")
    pywhatkit.playonyt(query)

# function to send mail
def sendMail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chiragsingh93135@gmail.com', 'password')
    server.sendmail('chiragsingh93135@gmail.com', to, content)
    server.close()