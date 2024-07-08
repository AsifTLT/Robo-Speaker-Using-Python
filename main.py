import pyttsx3

if __name__ == "__main__":
    print("Welcome To RoboSpeaker 1.1 Created by Asif ")
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter What You Want me to speak: ")
        if x.lower() == "q":
            engine.say("bye bye friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

