from Body.Listen import Listen
from Body.Speak import Speak

def MainExe():
    while True:
        query = Listen()
        if "hello" in query:
            Speak("Hi! I am Carnage!")
        elif "bye" in query:
            Speak("Good Bye Sir. Have a good day!")