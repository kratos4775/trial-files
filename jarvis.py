import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import time
import os





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio,language='en-in')
            print("You said...??????")
            print("You said..." + content )
        except Exception as e:
            print("please try again...")

    return content

def main_process():
    while True:
        #wishing
        #talking
        request = command().lower() 
        if "hello" in request:
            speak("hello sir,.. i am jarvis, how can i help you")
        elif"how r u" in request:
            speak("i am nice sir what about you")
        elif"namaste" in request:
            speak("namaste")
        elif"i am also nice" in request:
            speak("what are you doing today")
        elif"good morning" in request:
            speak("Good morning sir so whats going today")
        elif"good afternoon" in request:
            speak("Good afternoon sir ,.. how was your day")
        elif"good evening" in request:
            speak("Good evening sir,.. ")
        elif"good night" in request:
            speak("Good night sir take good sleep")
        elif"nice song jarvis" in request:
            speak("yes sir your choice is nice")
        elif"Jarvis" in request:
            speak("yes sir what happen")

            # songs codes 
        elif "play knife" in request:                                       # songs code
            speak("ok sir")
            webbrowser.open("https://www.youtube.com/watch?v=XrunlwIf2nA")

        elif "start my workout music" in request:
            speak("why not sir wait i am playing")
            webbrowser.open("https://www.youtube.com/watch?v=4DfVxVeqk2o&list=RDMM4DfVxVeqk2o&start_radio=1")

        elif "open history" in request:
            speak("")
            webbrowser.open("https://www.youtube.com/feed/you")

        elif "play wishes" in request:
            speak("ok sir")
            webbrowser.open("https://www.youtube.com/watch?v=Gz38Yj09k3A")

        elif "play " in request:
            speak("ok sir")
            webbrowser.open("")

        elif "start spotify" in request:
            speak("opening spotify sir")
            os.startfile(r"C:\Users\Pc\AppData\Roaming\Spotify\Spotify.exe")

            #controling functions
        elif "volume down" in request:
            pyautogui.hotkey("ctrl", "down")
        elif "volume down two times" in request:
            pyautogui.hotkey("ctrl", "down")
            pyautogui.hotkey("ctrl", "down")
            pyautogui.hotkey("ctrl", "down")

        elif "increase volume" in request:
            pyautogui.hotkey("ctrl", "up")
        elif "Jarvis increase" in request:
            pyautogui.hotkey( "up")
        elif "Jarvis decrease" in request:
            pyautogui.hotkey("down")
        elif "volume up two times" in request:
            pyautogui.hotkey("ctrl", "up")
            pyautogui.hotkey("ctrl", "up")
            pyautogui.hotkey("ctrl", "up")

        elif "next song" in request:
            pyautogui.hotkey("ctrl", "right")  
        elif "rewind" in request:
            pyautogui.hotkey("ctrl", "r")
            pyautogui.hotkey("ctrl", "r")
        elif"full screen" in request:
            pyautogui.press("f") 
        elif"exit" in request:
            pyautogui.press("Esc") 
        elif"resume" in request:
            pyautogui.press("space")
        elif"space" in request:
            pyautogui.press("space")
        elif"stop" in request:
            pyautogui.press("space")
        elif"play" in request:
            pyautogui.press("space")    
        
        elif "play next YouTube" in request:
            speak("ok sir")
            pyautogui.hotkey("shift","n")



            # random song code
        elif "play music" in request:
            speak("ok sir")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=4DfVxVeqk2o&list=RD4DfVxVeqk2o&start_radio=1")
            elif song  == 2:
                webbrowser.open("https://www.youtube.com/watch?v=XrunlwIf2nA&list=RDXrunlwIf2nA&start_radio=1&rv=XrunlwIf2nA&t=2")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=1OAjeECW90E")

               #common time date code 
        elif "time batao" in request:
            now_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("sir right now time is" + str(now_time))
        elif "date batao" in request:
            now_time = datetime.datetime.now().strftime("%B %d %y")
            speak("sir current date is" + str(now_time))

            #task adding system code
            #todo list
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                
                speak("Adding task : "+ task)
                with open ("todo.txt","a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                speak("work we have to do today is : " + file.read())

        elif "show task" in request: 
            with open ("todo.txt", "r") as file:
                task = file.read()
            notification.notify(
                title = "Today's work",
                message = task)

            #search  every app 
            #system
        elif "open physics wala" in request:
            speak("opening physics wallah sir")
            webbrowser.open("https://www.pw.live/study/batches/study")

        elif "open youtube" in request:
            speak("opening youtube.. sir")
            webbrowser.open("https://www.youtube.com/")

        elif "open chat" in request:
            speak("opening Chat GPT sir")
            webbrowser.open("https://chatgpt.com/")

        elif "close youtube" in request:
            speak("Closing YouTube")
            time.sleep(2)  # Give some time for the app to be open
            pyautogui.hotkey('alt', 'f4')  # This will close the active window        

        elif "open" in request:
            speak("ok sir")
            query = request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        
        elif "search google" in request:
            request = request.replace("jarvis","")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q="+ request)

        elif "search youtube" in request:
            speak("opening youtube application sir")
            request = request.replace("jarvis","")
            request = request.replace("search youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query="+ request)


            #wikipedia system questions
        elif "search wikipedia" in request:
            request = request.replace("jarvis ","")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)

            speak(result)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+917982469982", "kese ho ", 17, 3, 15, True, 2)

        # elif"send email" in request:
            # pwk.send_mail("ammodelcontact@gmail.com",user_config.gmail_password,"hello","hello, how are you","kodegukul@gmail.com")

        
        

       
main_process()
