
from selenium import webdriver
import time as tm
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


serv = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=serv)

mainSite = ('https://login.lg.com.br/login/accamargo')


def login():
    nav.get(mainSite)
    tm.sleep(1)
    nav.find_element('xpath' , '/html/body/div/div[2]/div/div[2]/main/div[1]/form/div[2]/div/input').send_keys('Henrico GAYZASSO') #primeiro input login
    tm.sleep(3)
    nav.find_element('xpath' , '/html/body/div/div[2]/div/div[2]/main/div[1]/form/div[3]/p/button/span[1]').click() #btn submit
     

login()