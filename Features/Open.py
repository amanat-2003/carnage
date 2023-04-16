import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


def OpenExe(Query):
    Query = str(Query).lower()

    if ("visit" in Query or "open" in Query or "launch" in Query or "start" in Query) and (".com" in Query or "website" in Query):
        if "open" in Query:
            Nameofweb = Query.replace("open ", "")
        elif "launch" in Query:
            Nameofweb = Query.replace("launch ", "")
        elif "start" in Query:
            Nameofweb = Query.replace("start ", "")
        elif "visit" in Query:
            Nameofweb = Query.replace("visit ", "")
        if ".com" in Nameofweb:
            Nameofweb = Nameofweb.replace(".com", "")
        elif "website" in Nameofweb:
            Nameofweb = Nameofweb.replace(" website", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query or "launch" in Query:
        if "open" in Query:
            Nameoftheapp = Query.replace("open ", "")
        elif "launch" in Query:
            Nameoftheapp = Query.replace("launch ", "")
        elif "start" in Query:
            Nameoftheapp = Query.replace("start ", "")
        sleep(0.1)
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

