import pyttsx3
import speech_recognition as sr
import webbrowser 
import time
import musiclibrary
import requests 
from dotenv import load_dotenv
import os
# from openai import OpenAI
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
 

def speak(text):
    print("Speaking: ", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # print("Speech Finished")

#     def aiprocess(command):
#         

#         completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[ {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Gooogle Cloud"},
#               {"role": "user", "content": "command"}
#     ]
# )

#         return completion.choices[0].message

def processCommand(c):
    print("Processing command:", command)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open Linkdin" in c.lower():
        webbrowser.open("https://Linkdin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link = musiclibrary.music[song]
        webbrowser.open(link) 

    elif "news" in c.lower():
        r = requests.get(
    "https://newsapi.org/v2/top-headlines",
    params={
        "country": "us",
        "apiKey": newsapi
    }
    )
        if r.status_code == 200:
        #parse the JSON resposnse
          data = r.json()

        # Extract the articles
        articles = data.get('articles', [])
        # print the headlines
        for article in articles:
            speak(article['title'])

    # else:
    #     #Let openai handle the request
    #     output = aiprocess(c)
    #     speak(output)
    #     pass
        

    



if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True: 
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                #  print("Listening...")
                 r.adjust_for_ambient_noise(source, duration=0.5)
                 audio = r.listen(source)
            word = r.recognize_google(audio)
            # print("Heard: ", word)

            if word.lower().strip() == "jarvis": 
                # print("Calling speak YES")
                speak("Hi sir, how can I help you?")

                # print("YES completed")

                time.sleep(1)
                
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    # print("Command: ", command)

                    processCommand(command)
          
                    

        # except Exception as e:
        #     print("Error; {0}".format(e))

        except sr.UnknownValueError:
            print("Could not understand audio") 

        # except sr.RequestError as e:
        #     print("Google API error:", e)

        except Exception as e:
            print("Error:", e)
