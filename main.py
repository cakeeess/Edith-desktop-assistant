import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("This is Edith. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Couldn't catch you, try again!")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example@mail.com', 'pswrd')
    server.sendmail('example@mail.com', to, content)
    server.close()


def openCamera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def executeCommand(command):
    try:
        if 'open notepad' in command:
            os.system("start notepad.exe")
            speak("Opening Notepad")

        elif 'open calculator' in command:
            os.system("start calc.exe")
            speak("Opening Calculator")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com/")
            speak("Opening Google")

        elif 'open stack overflow' in command:
            webbrowser.open("https://stackoverflow.com/")
            speak("Opening Stack Overflow")

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'search' in command:
            speak("What do you want to search for?")
            search_query = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'wikipedia' in command:
            speak('Searching Wikipedia...')
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'send email' in command:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Please provide the email address of the recipient.")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email.")

        elif 'open camera' in command:
            openCamera()

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            exit()

        else:
            speak("Sorry, I didn't understand that command.")

    except Exception as e:
        print(e)
        speak("Oops! An error occurred while executing the command.")


def execute_from_text():
    query = text_area.get("1.0", "end-1c").lower()
    if query != "":
        executeCommand(query)


def execute_from_voice():
    query = takeCommand().lower()
    if query != 'none':
        text_area.insert(tk.END, f"User said: {query}\n")
        executeCommand(query)



root = tk.Tk()
root.title("Edith <3")
root.configure(background='#e6ccff')

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, bg='black', fg='white')
text_area.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

button_text = tk.Button(root, text="Execute from Text", command=execute_from_text, bg='#d9b3ff')
button_text.grid(row=1, column=0, padx=5, pady=5)

button_voice = tk.Button(root, text="Execute from Voice", command=execute_from_voice, bg='#d9b3ff')
button_voice.grid(row=1, column=1, padx=5, pady=5)

button_quit = tk.Button(root, text="Quit", command=root.quit, bg='#d9b3ff')
button_quit.grid(row=1, column=2, padx=5, pady=5)

wishMe()


root.mainloop()
