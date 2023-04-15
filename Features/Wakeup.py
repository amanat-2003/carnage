import speech_recognition as sr
import os

# Listen Function
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:  
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        # pa-Guru-IN - for punjabi
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    print(f"You said: {query}")
    return query

def WakeupDetected():
    query = Listen().lower()
    if "wake up" in query:
        os.startfile(r"Main.py")
    else:
        pass

while True:
    WakeupDetected()