import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')#it takes microsoft api sapi5
voices = engine.getProperty('voices')#voices will get the voices of microsoft api
#there are 2 voices david and zira we can change it by 0 and 1 in print(voices[1].id)
engine.setProperty('voices', voices[0].id)

#it help chotu to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#this function is used for wishing good evening and all according to time
def wishme():
    hour=int(datetime.datetime.now().hour)
    speak('initializing Iris')
    print('initializing Iris')
    if hour>=0 and hour<12:
        speak("Good Morning Sarthak Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sarthak Sir")
    else:
        speak("Good Evening Sarthak Sir")
    speak("My name is Iris what can i do for you.")

#it takes microphone input from user and return string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listning...")
        r.pause_threshold = 0.5 #it is used when a pause of user is 1 sec it recognize the given data
        audio = r.listen(source) #recognizer will listen to source

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in") #it will use google for the search it can use bing and many other things
        print("Sir Said:",query) #it will be printed what we said

    except Exception as e:
        print(e) #if there is exception what it can nbot recognize it will print it and say dobara bol
        print("Can you please Pardon...")
        query = 'None'

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sarthak.saxena06@gmail.com', 'sarthakkrishnan')
    server.sendmail('krishnan.sarthak@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()
        #Logic for executing task based on query
        if 'wikipedia' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(result)
            speak(result)


        elif 'open youtube' in query.lower():
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'open google' in query.lower():
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open facebook' in query.lower():
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open amazon' in query.lower():
            url = "amazon.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            music_dir = 'C:\\Users\\krish\\Music\\fav'
            songs = os.listdir(music_dir)
            #print(songs)
            num1 = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num1]))

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #print(strTime)
            speak(f"sir, the time is{strTime}")


        elif 'mail to sarthak' in query.lower():
            try:
                speak("what Should i say?")
                content = takecommand()
                to = "krishnan.sarthak@gmail.com"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send the mail at the moment")

        elif 'open telegram' in query.lower():
            telepath = "C:\\Users\\krish\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telepath)

        elif 'code' in query.lower():
            codepath = "C:\\Users\\krish\\Downloads\\Sublime Text Build 3211 x64\\sublime_text.exe"
            os.startfile(codepath)

      
        elif 'sleep' in query.lower():
            exit()