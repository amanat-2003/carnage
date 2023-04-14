import speech_recognition as sr
from googletrans import Translator

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
        query = r.recognize_google(audio, language="pa-Guru-IN")
    except:
        return ""

    query = str(query).lower()
    return query

# Translation
def Translation(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    return data

# Complete Function
def ListenAndPrint():
    query = Listen()
    data = Translation(query)
    print(f'You: {data}')
    return data

ListenAndPrint()