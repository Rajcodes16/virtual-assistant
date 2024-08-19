import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import wikipedia as googlescrap
import webbrowser
import os
import pywhatkit
import random
import pywhatkit as kit
import sys
import pyautogui
from googlesearch import search
import time
import requests
import openai
import pyjokes
import tkinter as tk
from tkinter import scrolledtext
import phonenumbers
import tkinter as tk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
from googletrans import Translator
from ApiKeys import api_key_openai

output_text = None
output_variable = None




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<5:
        speak("Hello!")
    
    elif hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Foxtel, please tell me how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #output_variable.set(output_variable.get() +"listening...")
        print("listening...")
        r.pause_threshold = 3
        audio= r.listen(source)
    try:
       #output_variable.set(output_variable.get() +"Recognizing...")
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')
       output_variable.set(output_variable.get() +f"user said: {query}\n")
       print(f"user said: {query}")

    except Exception as e:
        #output_variable.set(output_variable.get() +"Say that again please...")
        print("Say that again please...")
        return "None"
    return query

api =api_key_openai
openai.api_key = api
#-----------------------------
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500, 
            stop=None,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"
    
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dc821be944fe492ab96d3f4e30e00a65'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

    

def google_search(keyword):
    search_url = f"https://www.google.com/search?q={keyword}"
    output_variable.set(output_variable.get() +"this is what i found on the web")
    speak("this is what i found on the web")
    pywhatkit.search(keyword)
    try:
        
        result=googlescrap.summary(keyword,3)
        output_variable.set(output_variable.get() +result)
        speak(result)

    except:
        output_variable.set(output_variable.get() +"no speakable data available")
class PrintCapture:
    def __init__(self, text_variable):
          self.text_variable = text_variable

    def write(self,text):
          self.text_variable.set(self.text_variable.get() + text)


def start_program():
    global output_text
    global output_variable  # Add this line to access the global variable
    output_text.delete("1.0", tk.END)  # Clear previous output
    output_text.insert(tk.END, "I am Foxtel, please tell me how can I help you\n")



    wishMe()
    while True:
        query = takeCommand().lower()

        if "what can you do" in query:
             speak("I can do lot of tdxhings, for example you can ask me time, date. I can open websites for you, launch applications, and can do many more things that humans cannot do")

        elif "open whatsapp" in  query:
                apath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2329.5.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"
                os.startfile(apath)

        elif "tell me the date" in query:
                current_date = datetime.date.today()
                speak(current_date)

        elif "how are you" in query:
             speak("I am fine , how can I help you sir") 

        elif "thank you" in query:
             speak("It's my pleasure sir, always ready to help you sir")

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            speak("Please Wait...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            output_variable.set(output_variable.get() + "According to wikipedia\n")
            output_variable.set(output_variable.get() +results)
            speak(results)

        elif 'search youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}") 

        elif "open whatsapp" in  query:
                apath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2329.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"
                os.startfile(apath)

        elif 'open youtube' in query:
            speak("what you will like to watch?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")
            continue

        elif 'close youtube' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'open google' in query:
            speak("what should i search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)
            continue

        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe ")

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'play movie' in query:
            npath = "E:\\movies"
            movie = os.listdir(npath)
            os.startfile(os.path.join(npath, random.choice(movie)))


        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        elif 'Lock the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'open notepad' in query:
            npath = ("c:\WINDOWS\system32\\notepad.exe")
            os.startfile(npath)

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")


        elif 'go to sleep' in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                output_variable.set(output_variable.get() +ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "tell me a joke" in  query:
                joke = pyjokes.get_joke()
                speak(joke) 
        
        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "close paint" in query:
                os.system("taskkill /f /im mspaint.exe")

        elif "tell me the news" in query:
                speak("please wait sir, fetching the latest news")
                news() 

        elif "who are you" in query:
               output_variable.set(output_variable.get() +'My Name Is Foxtel')
               output_variable.set(output_variable.get() +'I can Do Everything that my creator programmed me to do')
               speak('I can Do Everything that my creator programmed me to do')

        elif "where i am" in  query or "where we are" in  query:
                speak("wait sir, let me check") 
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    output_variable.set(output_variable.get() +ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country'] 
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak(("sorry sir, due to network issue i am not able to find where we are."))          
                    pass
        

        elif "who created you" in query:
            output_variable.set(output_variable.get() +'I created by Priyo,Ashesh and Tushar, I created with Python Language, in Visual Studio Code.')
            speak('I created by Priyo,Ashesh and Tushar, I created with Python Language, in Visual Studio Code.')


        elif 'open chrome' in query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif "open map" in  query or "show my location" in  query:
                google_maps_url = "https://www.google.com/maps/search/?api=1&query=Current+Location"
                webbrowser.open(google_maps_url)    

        elif "trace the phone number" in  query:
                from phonenumbers import geocoder,carrier
                speak("which phone number you want to trace sir")
                a = takeCommand().lower()
                result = phonenumbers.parse(f"{'+91'+ a}")
                Carrier = carrier.name_for_number(result, 'en')  
                Region = geocoder.description_for_number(result, 'en') 
                speak(Carrier)
                speak(Region)

        elif "activate how to do mod" in query:
                from pywikihow import search_wikihow
                speak("How to do mode is activated, please tell me what you want to know")
                how = takeCommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)  

        elif "how much power is left" in query or "how much power we have" in query or "battery" in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f" Sir our system have {percentage} percent battery")
                if percentage>=75:
                    speak("We have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage<=15:
                    speak("we have very low power, please connect to charging the system will shutdown very soon")

        elif "open" in query:
                from Dictapp import openappweb
                openappweb(query)
        elif "close" in query:
                from Dictapp import closeappweb
                closeappweb(query)


        elif "switch the window" in  query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab") 
                pyautogui.keyUp("alt")

        elif 'close chrome' in query:
            os.system("taskkill /f /im/chrome.exe")

        elif 'open chrome' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

        elif "" in query:
            search = query
            url = f"https://www.google.com/search?q={search}"
            pywhatkit.search(query)
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            output_variable.set(output_variable.get() +f"is {temp}")
            speak(f" is {temp}")
             
                  
        elif "write" in query or "calculate" in query:
                speak("Searching for the best answer.")
                ask = query#takecommand().lower()
                response = generate_response(ask)
                output_variable.set(output_variable.get() + response + "\n")
                speak(response)
                continue
        else:
            
            if query.lower() == "exit":
                output_variable.set(output_variable.get() + "Goodbye!")
                break;
            google_search(query)

        output_text.update_idletasks()

if __name__=="__main__":
    root = tk.Tk()
    root.title("Foxtel - Voice Assistant")

    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
    output_text.pack(padx=10, pady=10)
    output_text.config(state=tk.DISABLED)

    output_variable = tk.StringVar()
    sys.stdout = PrintCapture(output_variable)
    
    start_button = tk.Button(root, text="Start Foxtel", command=start_program)
    start_button.pack()

    root.mainloop()  
