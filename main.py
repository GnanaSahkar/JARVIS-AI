import datetime
import os
import random

import pyjokes
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia

from openai import OpenAI


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#todo Define an function called AI which Uses the OpenAI API to Gnerate Responcive Texts
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = r.recognize_google(audio, language="en-in")
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            say("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError:
            say("Sorry, my speech service is down.")
            return "Sorry, my speech service is down."
        except sr.WaitTimeoutError:
            say("Listening timed out, please try again.")
            return "Listening timed out, please try again."
        except KeyboardInterrupt:
            say("Listening stopped.")
            print("Listening stopped.")
            return "Listening stopped."
        except Exception as e:
            print(f"Error: {e}")
            say("Some error occurred. Sorry from Sahkar.")
            return "Some error occurred. Sorry from Sahkar."


def playSong(command):
    song = command.lower().replace("play the song","")
    say(f"playing the {song} on Youtube")
    pywhatkit.playonyt(song)

def serchImages(command):
    Images = command.lower().replace("show the images of","").split()
    url = f"https://www.google.com/search?tbm=isch&q={Images}"
    say(f"showing the Images of{Images}")
    webbrowser.open(url)

def searchPerson(command):
    person = command.lower().replace("who is","").split()
    info  =wikipedia.summary(person)
    print(info)
    say(info)

if __name__ == '__main__':
    print("This AI is Developed by Sahkar")
    #say("Hii there Jarvis Here, How Can I help with you")

    while True:
        command = takeCommand()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["gmail", "https://mail.google.com"],
            ["whatsapp", "https://web.whatsapp.com"],
            ["spotify", "https://www.spotify.com"]
        ]
        for site in sites:
            if f"open {site[0]}".lower() in command.lower():
                say(f"Opening {site[0]}, Sir...")
                webbrowser.open(site[1])

        if "play the song" in command.lower():
            playSong(command)

        if "show the images of" in command.lower():
            serchImages(command)

        if "is the time" in command.lower():
            hour = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minutes} minutes")

        '''if "using" in command.lower():
            ai(prompt=command)'''

        if "thank you" in command.lower():
            say("Your Welcome Sir,Let me Know if i can Assist With you")

        if "who is" in command:
            searchPerson(command)

        if "jokes" in command.lower():
            say(pyjokes.get_joke())

        if "hi jarvis" in command.lower():
            say(f"Hello there,Jarvis here, How could i help you")
        '''if "surendra" in command.lower():
            say("Final year Panimalar Student")'''
#todo:Replce the chatGPT API with the Gemini