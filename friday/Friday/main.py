import speech_recognition as sr
import webbrowser
import pyttsx3 as px
import musiclibrary
import requests
import pyjokes as pj
import time as tt
from gtts import gTTS
import pygame
import os
import random as rn
import qr




print("\n")
print("#######################################################################")
print("#######################################################################")
print("#######################################################################")
print('''
        
                           .__                               
__  _  __ ____ |  |   ____  ____   _____   ____  
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >
             \/          \/            \/     \/ 
             
             
            HELLO    I'AM FRIDAY   A I
 
 ''')
 
print("#######################################################################")
print("#######################################################################")
print("#######################################################################")


print('''

                                                 
_____    ____  ____  ____   ______ ______
\__  \ _/ ___\/ ___\/ __ \ /  ___//  ___/
 / __ \\  \__\  \__\  ___/ \___ \ \___ \ 
(____  /\___  >___  >___  >____  >____  >
     \/     \/    \/    \/     \/     \/ 
       .__                               
______ |  |   ____ _____    ______ ____  
\____ \|  | _/ __ \\__  \  /  ___// __ \ 
|  |_> >  |_\  ___/ / __ \_\___ \\  ___/ 
|   __/|____/\___  >____  /____  >\___  >
|__|             \/     \/     \/     \/ 

''')
print("\n")




# Initialize recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
en = px.init()



newsapi = "28c34d4659364725bca57f5c04dd5f5e"


# def speak(text):
#     en.say(text)
#     en.runAndWait()

# Initialize pygame mixer once
pygame.mixer.init()

def speak(text):
    # Convert text to speech and save as an mp3 file
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Load and play the mp3 file
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Keep the program running until the audio is done playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Unload the mp3 file from memory
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def processCommand(c):
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

    elif "open app web" in c_lower:
        webbrowser.open("https://web.whatsapp.com")

    elif "open saavn" in c_lower:
        webbrowser.open("https://jiosaavn.com")

    elif "open link in" in c_lower:
        webbrowser.open("https://www.linkedin.com")

    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")




    elif "news" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news.")

            


    elif "open instagram" in c_lower:
        webbrowser.open("https://instagram.com")

    elif "open calculator" in c_lower:
        webbrowser.open("D:\py-project\FRIDAY\calsi\index.html")

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

    elif "list song" in c_lower:
        webbrowser.open("D:/FRIDAY/musisclibrary.py")



    elif "one joke please" in c_lower:
        joke = pj.get_joke()
        print(joke)
        speak(joke)



    elif c_lower.startswith("play"):
        song = c_lower.split(" ", 1)[1]
        link = musiclibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")



    elif "open scanner" == c_lower:  # Exact match for "open scanner"
        qr.scan()




    else:
        webbrowser.open("https://search.brave.com/")
        speak("This may help you, sir.")
        # chat_with_friday(c)


if __name__ == "__main__":


    passw= "Panda"
    speak("Access required")
    print("#######################################################################")
    print("#######################################################################")
    print("#######################################################################")
    password= input("Access Required : ")


    if(passw != password):
        print("Access Denied")
        speak("Access denied")

    else:
        speak("Initializing Friday..........")
        while True:
            try:
                print("recognizing.........\n")
                with sr.Microphone() as source:
                    print("Listening......")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    word = recognizer.recognize_google(audio)

                    if "friday" in word.lower():
                        speak("Yes sir..")
                        with sr.Microphone() as source:
                            print("Friday active....")
                            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                            command = recognizer.recognize_google(audio)

                            processCommand(command)

            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                speak("Sorry, I couldn't reach the recognition service.")

            except sr.UnknownValueError:
                print("Could not understand the audio")
                # speak("Sorry, I didn't catch that.")

            except Exception as e:
                print(f"Friday error..... {e}")
                speak("An error occurred. Please try again.")
