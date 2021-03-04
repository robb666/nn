import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import re
import time

np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        # return self.output


class Activation_ReLU:
    def forward(self, inputs):
        # Remember input values
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
        return self.output


# layer1 = Layer_Dense(4, 3)
# layer1.forward(X)
# activation1 = Activation_ReLU()
# print(activation1.forward(layer1.output))


""" PZU """

### DOM ###
driver = webdriver.Chrome()

url = driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')

"""Sprawdza logowanie"""
def pzu_log():
    log = driver.find_element_by_id('input_1')
    log.send_keys('macgrzelak')
    pas = driver.find_element_by_id('input_2')
    pas.send_keys('02^27_Sb#cT')
    driver.find_element_by_css_selector('.credentials_input_submit').click()
    log = driver.find_element_by_id('Login:LoginScreen:LoginDV:username-inputEl')
    log.send_keys('macgrzelak')
    pas = driver.find_element_by_id('Login:LoginScreen:LoginDV:password-inputEl')
    pas.send_keys('02^27_Sb#cT')
    driver.find_element_by_id('Login:LoginScreen:LoginDV:submit').click()
    time.sleep(2)
    return driver


driver = pzu_log()
# print(driver.page_source)


soup = BeautifulSoup(driver.page_source, features="lxml")
# print(' '.join(soup.text))

# for link in soup:
#     print(link['id'])







for link in soup.findAll('a', attrs={"id": re.compile("(?!.*collapseEl.*)", re.I)}):
    print(link.text)

    # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, link.text))).click()











def find_all(tag):
    for link in soup.findAll(tag, attrs={"id": re.compile("(?!.*collapseEl.*)", re.I)}):
        print(link.text)
        # re.search('(Polisy)', link.text, re.I)
        # if txt := link.text:
        #     print(txt)
        # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), 'Konta')]"))).click()
        # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, "ext-element-1"))).click()

        try:
            WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, link.text))).click()
            # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Polisy')]"))).click()


        except Exception:
            WebDriverWait(driver, 9).until(EC.element_to_be_clickable((By.ID, 'TabBar:DesktopTab-btnInnerEl'))).click()



# print('divy !!!')
# find_all('div')
# print('tr !!!')
# find_all('tr')
# print('td !!!')
# find_all('td')
# print('table !!!')
# find_all('table')
# print('form !!!')
# find_all('form')
# print('tbody !!!')
# find_all('tbody')
# print('input !!!')
# find_all('input')
# print('a !!!')
# find_all('a')
# print('span !!!')
# find_all('span')
# print('id !!!')
# find_all('id')
# print('img !!!')
# find_all('img')


"""Buttons"""
# buttons = driver.find_elements_by_xpath(".//form//input[@type='button']")
# for button in buttons:
#     print(button.text)

# driver.find_elements_by_css_selector('input[type=button])

"""Wyszukanie po tekście"""
# WebDriverWait(driver, 4).until(EC.element_to_be_clickable
#                                ((By.XPATH, f"//*[contains(text(), '{text}')]")))
















