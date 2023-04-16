from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.speak import Speak
import pathlib
from Body.listen import MicExecution

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_argument('--log-level=3')
# options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
Speak("Initializing The Whatsapp Software.")

ListWeb = {'papa' : "+919417637599",
            'muma': "+918427177499",
            "mma": '+918427177499'}

def WhatsappSender(Name):   
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        print("1")
        driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        print("2")
        Speak("Message Sent")
        print("3")
        driver.switch_to.window(driver.window_handles[-1])
        print("4")
        driver.close()
        
    except:
        print("Invalid Number")
