from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import re


options = Options()
options.add_argument('--window-size=2220,1080')
driver = webdriver.Chrome(options=options)

driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')
log = driver.find_element_by_id('input_1')
log.send_keys('macgrzelak')
pas = driver.find_element_by_id('input_2')
pas.send_keys('03*29_Ps&bY')
driver.find_element_by_css_selector('.credentials_input_submit').click()
log = driver.find_element_by_id('Login:LoginScreen:LoginDV:username-inputEl')
log.send_keys('macgrzelak')
pas = driver.find_element_by_id('Login:LoginScreen:LoginDV:password-inputEl')
pas.send_keys('03*29_Ps&bY')
driver.find_element_by_id('Login:LoginScreen:LoginDV:submit').click()
# time.sleep(2)
# WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Konta']"))).click()
time.sleep(3)


tasks = ['konta', 'transakcje', 'podmioty', 'edytuj podmiot']
personal_data = {'imię': 'robert', 'nazwisko': 'grzelak', 'pesel': '82082407038'}



for phrase in tasks:
    # for phrase in tasks:
    print(phrase)
    if phrase not in ('\n', '', ' ') and re.search(phrase, page_source, re.I):
        print(phrase)
        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                              f"//*[contains(text(), '{phrase.title()}')]"))).click()

            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                    f"//*[contains(@type, 'text') and @role='textbox']"))).send_keys('Robert')



        except Exception as e:
            print(f'{e} - exception!')
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                            f"//*[text()='Konta']"))).click()









