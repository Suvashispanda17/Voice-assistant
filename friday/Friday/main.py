import pyttsx3 as px
import speech_recognition as sr
import webbrowser 
import cowsay as cs 
import musiclibrary
import password
import qr 
import pyjokes as pj 
import random as rn
import requests as re
import google.generativeai as ai
import getpass 
from datetime import datetime
import wikipedia


#################################
en = px.init()
#################################
newsapi = "<read line 26 >"
################################


##########################################################
# using google api for commands for backend
API_KEY='<generate your own api key idiottt!!>'

ai.configure(api_key=API_KEY)
model=ai.GenerativeModel("gemini-pro")
chat= model.start_chat()
def scan(command):
    while True:
        message= command
        if message.lower() =="bye":
            print("Friday: goodbye")
            break
        response=chat.send_message(message)
        clean=  response.text.replace("*","")
        print("Friday: ",clean)
        speak(clean)
################################
print("\n")
print("#######################################################################")
print("#######################################################################")
print("#######################################################################")
print(r'''
        
                                       .__                               
                        __  _  __ ____ |  |   ____  ____   _____   ____  
                        \ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
                         \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
                          \/\_/  \___  >____/\___  >____/|__|_|  /\___ >
                                     \/          \/            \/     \/ 
                                    
                                    
                                                           HELLO    I'AM FRIDAY   A I
 
 ''')
 
print("#######################################################################")
print("#######################################################################")
print("#######################################################################")


print(r'''

                                                    
                            _____    ____  ____  ____   ______ ______
                            \__  \ _/ ___\/ ___\/ __ \ /  ___//  ___/
                            / __ \\  \__\  \__\  ___/ \___ \ \___ \ 
                            (____  /\___  >___  >___  >____  >____  >
                                \/     \/    \/    \/     \/     \/ 
      

      *****************************Friday: I AM HERE TO HELP YOU AND MAKE IT EASY FOR YOU TO USE ME.**************************************
                                   >_                              
                            ______ |  |   ____ _____    ______ ____  
                            \____ \|  | _/ __ \\__  \  /  ___// __ \ 
                            |  |_> >  |_\  ___/ / __ \_\___ \\  ___/ 
                            |   __/|____/\___  >____  /____  >\___  >
                            |__|             \/     \/     \/     \/ 

''')
print("\n")

###############################################################
# this function is used to convert text to speech
def speak(text):
    en.say(text)
    en.runAndWait()

###############################################################################
def processcommand(c):
    c_lower = c.lower()


    if "open google" in c_lower:
        webbrowser.open("https://google.com")

    elif "open internet speed" in c_lower:
        webbrowser.open("https://fiber.google.com")

    elif "open gmail" in c_lower:
        webbrowser.open("https://mail.google.com")

    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")

    elif "open chat gpt" in c_lower:
        webbrowser.open("https://chatgpt.com")

    elif "open chat-box" in c_lower:
        webbrowser.open("https://web.whatsapp.com")

    elif "open saavn" in c_lower:
        webbrowser.open("https://jiosaavn.com")

    elif "open link in" in c_lower:
        webbrowser.open("https://www.linkedin.com")

    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c_lower:
        webbrowser.open("https://instagram.com")

    elif "open calculator" in c_lower:
        webbrowser.open("file:///C:/Users/suvas/OneDrive/Desktop/PROJECTS/voice-assistant/connections/calsi/index.html")

    elif "play songs" in c_lower:
        music = {
            "faded": "https://youtu.be/60ItHLz5WEA?si=mmSKUobSmpT6ukCg",
            "play": "https://youtu.be/YQRHrco73g4?si=MoenHNDelrX6c8SH",
            "darkside": "https://youtu.be/M-P4QBt-FWw?si=H_Ub8ek-Rg7bj7pe",
            "knox": "https://youtu.be/T5rmd-vKQeM?si=dheBme3ySU4rXnD9",
            "knox2": "https://youtu.be/Z_URRM9prsc?si=BkXhcfO7-kDba6Ok",
            "mashup": "https://youtu.be/q6bBriGtMaE?si=4GWHbqHbE6A60KeT",
            "honeysingh playlist": "https://www.youtube.com/watch?v=NbyHNASFi6U&list=RDEMulALs7qwkePpaGzHG_ttvg&start_radio=1",
            "teluguplaylist": "https://www.youtube.com/watch?v=VQ2-HPwxAZY&list=RDQMg5xeA07Wevs&start_radio=1",
            "saavn": "https://jiosaavn.com",
            "thumkeshwari": "https://youtu.be/Qfe5F7nXkKQ?si=XgBHiYUCmOjDEgFx",
            "trending": "https://open.spotify.com/playlist/653Lsnp17BbhKumhrFt80e?si=1FoCi0iyTASrjm_iV1njXA&pi=a-06U_xFeSRZOY"
        }

        random_song = rn.choice(list(music.keys()))
        webbrowser.open(music[random_song])


    elif "who made you" in c_lower or "who created you" in c_lower: 
            speak("made by team 15 suvashis panda  paramesh srikanth")


    elif 'wikipedia' in c_lower:
        query = c_lower.replace("wikipedia", "").strip()
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "list song" in c_lower:
        webbrowser.open("D:/FRIDAY/musisclibrary.py")
    elif "today's date" in c_lower :
        now = datetime.now()
        print("Current Date and Time: ", now)
        speak("Today's date and time is " + now.strftime("%Y-%m-%d %H:%M:%S"))

    elif "generate password" in c_lower:
        password.pas()

    elif "one joke please" in c_lower:
        joke = pj.get_joke()
        cs.tux("\n".joke,"\n")
        speak(joke)

    elif "news" in c_lower:

        rs = re.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if rs. status_code == 200:
            data = rs.json()
            articles = data.get["articles",[]]

            for article in articles:
                speak(article["title"])


    elif c_lower.startswith("play"):
        song = c_lower.split(" ", 1)[1]
        link = musiclibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")



    elif "open scanner" == c_lower:  
        qr.scan()


    else:
        # google handling the request 
        scan(c)


if __name__ == "__main__":
    while True:
        passw = "TEAM15"
        speak("Access required")
        print("#######################################################################")
        print("#######################################################################")
        print("#######################################################################")
        password = getpass.getpass("Access Required : ")

        if passw != password:
            print("Access Denied")
            speak("Access denied")
        else:
            speak("Access granted")
            cs.tux("\nWelcome to Friday!\n\n")
            speak("Welcome, boss")

            # Once access is granted, start recognizing commands
            while True:
                recogniser = sr.Recognizer()

                print("\n\nRecognizing...\n\n")
                try:
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = recogniser.listen(source, timeout=5, phrase_time_limit=5)

                    word = recogniser.recognize_google(audio)
                    if word.lower() == "friday":
                        speak("Yes, sir")

                        with sr.Microphone() as source:
                            print("\nFriday active...")
                            audio = recogniser.listen(source)
                            command = recogniser.recognize_google(audio)

                            processcommand(command)

                except sr.UnknownValueError:
                    cs.cheese("QUERY ERROR --> PLEASE TRY AGAIN ")
                except Exception as e:
                    cs.cow(f"Could not request results; {e}\n")
                 

        
