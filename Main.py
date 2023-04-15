from Body.listen import ListenTranslatePrint
from Body.speak import Speak
from Features.Clap import Tester

def Main():
    Tester()
    Speak("Welcome Amanat Singh!")
    while True:
        query = ListenTranslatePrint()
        print(query)


if __name__ == "__main__":
    Main()