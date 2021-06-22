import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def slicer(my_str, sub):
    index = my_str.find(sub)

    if index != -1:
        return my_str[index:]
    else:
        raise Exception('Sub string not found!')

def takeCommand():
    # takes my command from microphone and gives text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[hyp] Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("[hyp] Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if 'hey michael' in query.lower():
            commandQuery = r.recognize_google(audio, language='en-in')
            commandQuery = commandQuery.lower()
            commandQuery = commandQuery.replace('hey michael', '')
            print("[hyp] User said: " + query)
        else:
            return "None"
    except Exception as e:
        return "None"
    return commandQuery


if __name__ == "__main__":
    print("[hyp] Starting Michael, your virtual assitant.")
    speak("How can I help you today?")
    while True:
        command = takeCommand().lower()
        if 'wikipedia' in command:
            speak("Searching on wikipedia")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'play' in command:
            song = command.replace('play', '')
            speak("Playing " + song + " on YouTube")
            print("Playing " + song + " on YouTube")
            pywhatkit.playonyt(song, use_api=True)
        elif 'search on the internet' in command:
            search = command.replace('search on the internet', '')
            speak("Searching " + search + " on Google")
            pywhatkit.search(search)
        elif 'open' in command:
            try:
                appname = command.replace('open', '')
                os.system("start " + appname)
                speak('Opening ' + appname)
            except Exception as e:
                speak("An error occurred")
                print(e)
        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strTime)
        elif 'stop' in command:
            speak("Bye, Bye")
            exit()
