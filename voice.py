import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")

def speechtotxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    # if sptext().lower() == "hey dude" :
    while True:   
        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is dude"
            speechtotxt(name)

        elif "old are you" in data1:
            age = "i am two years old"
            speechtotxt(age)

        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtotxt(time)

        elif 'youtube' in data1:
            webbrowser.open("http://www.youtube.com/")

        elif 'google' in data1:
            webbrowser.open("google.com/")

        elif 'instagram' in data1:
            webbrowser.open("instagram.com/")

        elif 'web' in data1:
            webbrowser.open("https://www.wscubetech.com/")

        elif 'chatgpt' in data1:
            webbrowser.open("chatgpt.com")

        elif "jokes" in data1:
            joke_1 = pyjokes.get_joke(language="en",category="neutral")
            print(joke_1)
            speechtotxt(joke_1)
        
        elif 'play song' in data1:
            add = "E:\rk_music"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[0]))

        elif 'exit' in data1:
            speechtotxt("thank you")
            break









    # else:
    #     print("thanks")
