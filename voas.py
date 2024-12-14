import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import requests
import pywhatkit as kit
import pyautogui
import pytz
from PIL import Image
from astral import LocationInfo
from astral.sun import sun
from playsound import playsound
import yfinance as yf
import wolframalpha
from tkinter import Tk, Label, Button

# Initialize text-to-speech engine
def speechtotxt(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()
        except sr.UnknownValueError:
            speechtotxt("Sorry, I didn't understand that.")
            return ""

# Get current time
def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

# Get weather info
def get_weather(city):
    api_key = "48db63e25b3540988c8182530241412"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city} is {weather_desc} with a temperature of {temperature} degrees Celsius."
    else:
        return "Sorry, I couldn't fetch the weather details."

# Get financial stock info
def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get('regularMarketPrice')  # Safely fetch price
        if price:
            return f"The current price of {ticker} is {price} USD."
        else:
            return "Sorry, I couldn't fetch the stock price. Please check the ticker symbol."
    except Exception as e:
        return f"An error occurred while fetching the stock price: {str(e)}"

# Perform WolframAlpha query
def ask_wolfram(query):
    app_id = "your_wolframalpha_api_key"  # Replace with your WolframAlpha API key
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    return next(res.results).text

# Astronomical info
def get_sun_times():
    city = LocationInfo("London", "England", "Europe/London", 51.5, -0.1)
    s = sun(city.observer)
    sunrise = s['sunrise'].strftime("%H:%M")
    sunset = s['sunset'].strftime("%H:%M")
    return f"In London, sunrise is at {sunrise} and sunset is at {sunset}."

# Command execution function
def execute_command():
    speechtotxt("How can I assist you today?")
    while True:
        command = sptext()

        if "your name" in command:
            speechtotxt("My name is Dude, your voice assistant.")
        elif "how are you" in command:
            speechtotxt("I am good, what about you")
        elif "please help me" in command:
            speechtotxt("how can i help you")
        elif "who are you" in command:
            speechtotxt("i am dude, made by rishabh")

        elif "time" in command:
            current_time = get_time()
            speechtotxt(f"The current time is {current_time}.")

        elif "weather" in command:
            speechtotxt("Which city's weather would you like to know?")
            city = sptext()
            weather = get_weather(city)
            speechtotxt(weather)

        elif "play a song" in command:
            add = "E:\\rk_music"
            listsong = os.listdir(add)
            os.startfile(os.path.join(add, listsong[0]))

        elif "youtube" in command:
            speechtotxt("Opening YouTube.")
            webbrowser.open("http://www.youtube.com/")

        elif "google" in command:
            speechtotxt("Opening Google.")
            webbrowser.open("http://www.google.com/")

        elif "play" in command:
            song = command.replace("play", "")
            speechtotxt(f"Playing {song} on YouTube.")
            kit.playonyt(song)

        elif "joke" in command:
            joke = pyjokes.get_joke()
            speechtotxt(joke)

        elif "chatgpt" in command:
            webbrowser.open("chatgpt.com/")

        elif "instagram" in command:
            webbrowser.open("instagram.com")

        elif "screenshot" in command:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speechtotxt("Screenshot taken.")

        elif "stock price" in command:
            speechtotxt("Please provide the stock ticker symbol, such as GOOGL for Google or TATAMOTORS.NS for Tata Motors.")
            ticker = sptext()
            stock_price = get_stock_price(ticker.upper())
            speechtotxt(stock_price)

        elif "sunrise" in command or "sunset" in command:
            sun_times = get_sun_times()
            speechtotxt(sun_times)

        elif "exit" in command or "bye" in command:
            speechtotxt("Goodbye! Have a great day!")
            break

        else:
            speechtotxt("I didn't understand that. Please try again.")

# GUI Implementation
def start_gui():
    root = Tk()
    root.title("Voice Assistant")
    root.geometry("400x200")
    
    Label(root, text="Voice Assistant", font=("Arial", 20)).pack(pady=10)
    Button(root, text="Start", command=execute_command, font=("Arial", 15), bg="green", fg="white").pack(pady=10)
    Button(root, text="Exit", command=root.destroy, font=("Arial", 15), bg="red", fg="white").pack(pady=10)
    
    root.mainloop()

# Start GUI
start_gui()
