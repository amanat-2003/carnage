from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.listen import MicExecution
from time import sleep
print('>> Starting the Carnage : Wait for some seconds.')
from Body.speak import Speak
from Features.Clap import Tester
print('>> Starting the Carnage : Wait for few seconds more')

def MainExecution():

    Speak("Hello, Ammaanat. How are you?")
    sleep(3)
    Speak("I'm Carnage, I'm ready to assist you sir.")
    while True:
        Data = MicExecution()
        Data = str(Data)
        if len(Data) <= 3:
            continue
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data: 
            Reply = QuestionsAnswer(Data)
        else:
            Reply = ReplyBrain(Data)
        Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
