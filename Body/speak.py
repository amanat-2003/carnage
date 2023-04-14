# Speak Functions

# Windows based - pip install pyttsx3
# Chrome based - pip install selenium==4.1.3


import pyttsx3

# Windows based
# Advantages = Fast, Offline
# Disadvantages = Overspeak, Less no. of voices
def SpeakNative(txt):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    print("")
    print(f"Me: {txt}")
    print("")
    engine.say(txt)
    engine.runAndWait()

# Chrome Based
# Advantages = More voices, More clear, Overspeaking
# Disadvantages = Word Limit, Slow

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "Database\\chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(txt):
    lengthoftext = len(str(txt))

    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"Me: {txt}.")
        print("")
        Data = str(txt)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()   

        if lengthoftext >= 30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100:
            sleep(13)
        elif lengthoftext>=120:
            sleep(14)
        else:
            sleep(2)
