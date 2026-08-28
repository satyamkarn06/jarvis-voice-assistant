import pyttsx3

engine = pyttsx3.init()

for i in range(5):
    print(i)
    engine.say("ya")
    engine.runAndWait()