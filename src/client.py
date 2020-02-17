import pyttsx3 # Text to speech conversion library
import speech_recognition as sr  # For recognizing voice
import datetime
import wikipedia # for searching in wikipedia
# import webbrowser
# import os
# import smtplib
import requests, json
from collections import OrderedDict


#APPOWNER = 'Priyank Saluja'
engine = pyttsx3.init('sapi5') #object creation
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #changing index, changes voices. 1 for male & 0 for female
rate = engine.getProperty('rate') #getting details of current speaking rate
engine.setProperty('rate', 140) #setting up new voice rate
url = 'http://127.0.0.1:8000/user/' #API URL


def speak(text):
    '''
    :param text: Text that needs to be pronounced
    :return: NULL .. it will just pronounce the text
    Description: This function will pronounce the string passed to it
    '''
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def senddatatoserver(data, resource):
    try:
        endpoint = url + resource
        response = requests.post(endpoint, data=json.dumps(data), headers={'Content-Type':'application/json'})
        return True if response.status_code in (200, 201) else False
    except Exception as e:
        #print (str(e))
        return False


def welcomeuser():
    '''
    Description: Wish user based on current system time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak ("Good Morning... ")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon... ")
    else:
        speak("Good Evening... ")


def inputcommand(text2ask):
    '''
    :param text2ask: text that program should convert to audio and speak
    :return: convert captured audio to text and returns it
    recognize_sphinx: Works offline
    recognize_google: Require Internet connection
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            #print("Listening...")
            speak(text2ask)
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-GB')
                return query
            except Exception as e:
                speak("Invalid entry.. Please repeat...")


def user_registration():
    '''
    :Description: Pass form fields to input command function for input from user and get text in return and create a tuple and will call platform APIs to save data
    '''
    formvalues = []
    textforuserinput = ['What is your first name', 'What is your last name', 'What is your age']
    for text in textforuserinput:
        query = inputcommand(text)
        formvalues.append(query.replace(' ', ''))
    speak("Please wait while I process your data")
    form_data = {
        'first_name': formvalues[0],
        'last_name': formvalues[1],
        'age': int(formvalues[2]),
        'request_type': 'User Registration',
        'host': 'Terminal 1',
        'keywords': 'User Registration'
    }
    response = senddatatoserver(form_data, 'register')
    text = "User registered successfully" if response else "Registration failed.. Please try again after some time"
    speak(text)


def seachwikipedia():
    '''
    :Description: Pass form fields to input command function for input from user and get text in return and search the same in wikipedia
    and speak first 2 lines of it and also will call platform APIs to save data
    '''
    query = inputcommand("What you would like to search in wikipedia.. Just say the keywords")
    if query:
        speak('Searching wikipedia for {}'.format(query))
        try:
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        except:
            speak("Unable to find {} in wikipedia".format(query))

    # Insert data to database via API
    try:
        form_data = {
            'first_name': 'Wiki User',
            'last_name': 'Wiki User',
            'age': 0,
            'request_type': 'Wiki Search',
            'host': 'Terminal 1',
            'keywords': query
            }
        senddatatoserver(form_data, 'register')
    except:
        pass


def getuserinput():
    '''
    Take input from user - 1 for wikipedia and 2 for registration form.
    Pass the control the respective function
    '''
    try:
        speak("I am here to help you..")
        executefunction = True
        # Define keywords and function as key value pair for prompting to user
        # key would be words you wanted to speak to user for input and value would be function name
        useroptions = OrderedDict()
        useroptions['Please say wiki for wikipedia'] = 'seachwikipedia'
        useroptions['Please say register for user registration form'] = 'user_registration'
        text2ask = ''
        for key in useroptions.keys():
            text2ask = text2ask + ' ' + key

        while executefunction:
            query = inputcommand(text2ask)
            for key in useroptions.keys():
                res = useroptions[key] if str(query.lower()) in key else None
                if res is not None:
                    executefunction = False
                    eval(res)()
                    break
            if res is None:
                speak("Invalid Input.. Please try again !!")
    except:
        speak("There seems to be some issue.. Please try after some time !!")

    speak("Thanks for your visit. Please share your feedback ")


if __name__ == '__main__':
    welcomeuser()
    getuserinput()
