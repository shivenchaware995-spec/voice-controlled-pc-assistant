import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import psutil
import pyautogui
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            command = r.recognize_google(audio).lower()

            print("You:", command)
            return command

        except:
            speak("Sorry, I did not understand.")
            return ""

def execute(command):

    if "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye.")
        return False

    elif "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "open chrome" in command:
        speak("Opening Chrome.")
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )

    elif "open vs code" in command:
        speak("Opening Visual Studio Code.")
        subprocess.Popen("code")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "search youtube" in command:
        query = command.replace("search youtube", "").strip()

        if query:
            speak("Searching YouTube for " + query)
            webbrowser.open(
                "https://www.youtube.com/results?search_query="
                + query.replace(" ", "+")
            )

    elif "search google" in command:
        query = command.replace("search google", "").strip()

        if query:
            speak("Searching Google for " + query)
            webbrowser.open(
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )

    elif "open downloads" in command:
        speak("Opening Downloads.")
        os.startfile(os.path.expanduser("~/Downloads"))

    elif "open desktop" in command:
        speak("Opening Desktop.")
        os.startfile(os.path.expanduser("~/Desktop"))

    elif "take screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        speak("Screenshot saved.")

    elif "system information" in command:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        speak("CPU usage is " + str(cpu) + " percent")
        speak("Memory usage is " + str(ram) + " percent")

    elif "open calculator" in command:
        speak("Opening calculator.")
        subprocess.Popen("calc.exe")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        subprocess.Popen("notepad.exe")

    elif command:
        speak("I will search that for you.")
        webbrowser.open(
            "https://www.google.com/search?q="
            + command.replace(" ", "+")
        )

    return True

def main():

    speak("Voice assistant started.")
    speak("How can I help you?")

    while True:

        command = listen()

        if command:

            if execute(command) == False:
                break

main()