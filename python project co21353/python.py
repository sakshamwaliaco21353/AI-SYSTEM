import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print('listening')
        audio =r.listen(source)

    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query} ")

    except:
        print("say that again please...")
        return "None"

    return query

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")
    print("i am Mr saksham walia sir , how may i help you")
    speak("i am Mr saksham walia sir , how may i help you")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

wish_me()
while True:
    query= takecommand().lower()

    if  "wikipedia" in query:
         speak("searching in wikipedia...")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak(results)
         print(results.lower())
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open bank" in query:
        webbrowser.open("https://www.onlinesbi.com")
        webbrowser.open("https://www.axisbank.com")
        webbrowser.open("https://www.hdfcbank.com")
    elif "time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(strTime)
    elif "go to sleep" in query:
        speak("Going to sleep sir ")
        break

print("THAnk you project created by saksham walia co21353")