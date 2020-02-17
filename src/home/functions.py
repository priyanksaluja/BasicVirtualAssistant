
import pyttsx3 # Text to speech conversion library
import speech_recognition as sr  # For recognizing voice
import datetime
import wikipedia # for searching in wikipedia
import webbrowser
import os
import smtplib


APPOWNER = 'Priyank Saluja'
engine = pyttsx3.init('sapi5') #object creation
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #changing index, changes voices. 1 for male & 0 for female
rate = engine.getProperty('rate') # getting details of current speaking rate
engine.setProperty('rate', 140) # setting up new voice rate

def speak(text):
    '''
    :param text: Text that needs to be pronounced
    :return: NULL .. it will just pronounce the text
    Description: This function will pronounce the string passed to it
    '''
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak ("Good Morning "+ APPOWNER)
    elif hour >=12 and hour < 18:
        speak("Good Afternoon " + APPOWNER)
    else:
        speak("Good Evening " + APPOWNER)

def inputCommand(text2ask):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        speak(text2ask)
        audio = r.listen(source)

        try:
            print("Recognizing")
            query=r.recognize_google(audio, language='en-IN')
            print("User said: {}".format(query))
            speak(query)
        except Exception as e:
            print("Please repeat...")
            query = None
        return query

speak("This is a test message")
wishMe()
myform = {
    'Spellyourfirstname': '',
    'LastName': '',
    'age': '',
    'Gender': ''
    }
for key in myform.keys():
    text2ask = key
    query = inputCommand(text2ask)
    myform[key] = query.replace(' ', '')

print (myform)

# Perform task as per query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    speak(results)