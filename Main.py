from Body.Listen import ListenTranslatePrint
from Body.Speak import Speak
from Features.Clap import Tester

def Main():
    Tester()
    Speak("Welcome Amanat Singh!")
    while True:
        query = ListenTranslatePrint()
        print(query)


if __name__ == "__main__":
    Main()