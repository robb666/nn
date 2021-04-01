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
from skimage import io as in_out
import matplotlib.pyplot as plt
import webp
import os
from PIL import Image
from wand.image import Image as wi
import pytesseract
import io
import cv2


print(pytesseract.get_tesseract_version())

# np.random.seed(0)
#
# X = [[1, 2, 3, 2.5],
#      [2.0, 5.0, -1.0, 2.0],
#      [-1.5, 2.7, 3.3, -0.8]]
#
#
# class Layer_Dense:
#     def __init__(self, n_inputs, n_neurons):
#         self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
#         self.biases = np.zeros((1, n_neurons))
#
#     def forward(self, inputs):
#         self.output = np.dot(inputs, self.weights) + self.biases
#         # return self.output
#
#
# class Activation_ReLU:
#     def forward(self, inputs):
#         # Remember input values
#         self.inputs = inputs
#         self.output = np.maximum(0, inputs)
#         return self.output


# layer1 = Layer_Dense(4, 3)
# layer1.forward(X)
# activation1 = Activation_ReLU()
# print(activation1.forward(layer1.output))





class BoT:

    options = Options()
    options.add_argument('--window-size=2220,1080')
    driver = webdriver.Chrome(options=options)

    def __init__(self, url, tasks, personal_data):
        self.url = url
        self.tasks = tasks
        self.personal_data = personal_data
        # self.cv2 = cv2

    def get_url(self):
        self.driver.get(self.url)

    def find_id(self, element):
        self.locator = self.driver.find_element_by_id(element)
        return self.locator

    def find_css(self, element):
        self.locator = self.driver.find_element_by_css_selector(element)
        return self.locator

    def find_xpath(self, element):
        self.locator = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, element)))
        return self.locator

    def send_keys(self, keys):
        self.locator.send_keys(keys)

    def page_source(self):
        self.next_page_source = BeautifulSoup(self.driver.page_source, features="lxml").get_text()
        return self.next_page_source

    def screen_shot(self):
        return self.driver.save_screenshot(f"screenshot.png")

    # @staticmethod
    def image_manipulation(self):
        png = cv2.imread(os.getcwd() + f'/screenshot.png')
        self.grey = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
        return self.grey

    # @staticmethod
    def ocr_text(self):
        self.ocr = []
        ocr_raw = pytesseract.image_to_string(self.grey, lang='pol').split()
        for raw in ocr_raw:
            if raw not in ('_', '|', '-', '—', '*', '=', 'E', 'v', 'V', 'p', 'T', 'ZŁ', '©', '-MM-dd', 'E#', '?', '.'):
                self.ocr.append(raw)
        return self.ocr

    def task_execution(self):
        for phrase in tasks:
            if phrase := re.search(phrase, page_source, re.I):  # Make case insensitive.
                re_phrase = phrase.group()
                # print(re_phrase)
                try:
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                   f"//*[contains(text(), '{re_phrase}')]"))).click()
                except:
                    print('Problem z wykonaniem zadania !')

    def form_fill(self):
        for k, v in personal_data.items():
            print('!page source: ' + self.next_page_source)
            if key := re.search(k, self.next_page_source, re.I):
                re_k = key.group()
                try:
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                f"//*[contains(text(), '{re_k}')]/following::input[1]"))).send_keys(v)
                except:
                    print('Brak BOXa !')
                    pass
                    # WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                    #                                                             f"//*[text()='Wyszukiwanie']"))).click()

    def wysiwyg(self):
        for ocr_txt in self.ocr:
            print('!ocr: ', self.ocr)
            ocr_txt = re.sub('[|]', '', ocr_txt)
            if ocr_txt not in ('\n', '', ' ') and (ocr_txt := re.search(re.escape(ocr_txt), self.next_page_source, re.I)):
                ocr_phrase = ocr_txt.group()
                print(ocr_phrase)
                try:
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                   f"//*[contains(text(), '{ocr_phrase}')]"))).click()
                    try:
                        self.form_fill()
                    except:
                        pass

                except:
                    print('Brak screena !')
                    # self.page_source()
                    self.screen_shot()
                    self.image_manipulation()
                    self.ocr_text()
                    self.wysiwyg()
                    pass
                    # WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                    #                                                             f"//*[text()='Wyszukiwanie']"))).click()

                    # photo = in_out.imread(os.getcwd() + f"/screenshot.png")
                    # plt.imshow(photo)
                    # plt.show()
                    # print(photo.shape)
                    # pdf = wi(filename=photo, resolution=250)
                    # return scr
                    # break

                # tasks.pop(0)
                # tag = 'tbody'
                # find_all(tag, tasks)
                # webp.save_image(scr, 'image.webp', quality=50)
                # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Ofert')]"))).click()



url = 'https://everest.pzu.pl/pc/PolicyCenter.do'

tasks = ['konta', 'transakcje', 'podmioty', 'edytuj podmiot']

personal_data = {'imię': 'robert', 'nazwisko': 'grzelak', 'PESEL': '82082407038', 'REGON': '123456789', 'PIN': '1568',
                 'numer rejestracyjny': 'EL4C079', 'VIN': 'WWWZZZ456SD8'}


bot = BoT(url, tasks, personal_data)
bot.get_url()
bot.find_id('input_1')
bot.send_keys(keys='macgrzelak')
bot.find_id('input_2')
bot.send_keys(keys='03*29_Ps&bY')
bot.find_css('.credentials_input_submit').click()
bot.find_id('Login:LoginScreen:LoginDV:username-inputEl')
bot.send_keys(keys='macgrzelak')
bot.find_id('Login:LoginScreen:LoginDV:password-inputEl')
bot.send_keys(keys='03*29_Ps&bY')
bot.find_id('Login:LoginScreen:LoginDV:submit').click()
time.sleep(2)
# bot.find_xpath("//*[text()='Wyszukiwanie']").click()
# bot.sleep(3)

page_source = bot.page_source()
bot.screen_shot()
grey = bot.image_manipulation()
ocr = bot.ocr_text()
# print(ocr)


# bot.task_execution()
# bot.form_fill()
bot.wysiwyg()






# self.driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')
# log = self.driver.find_element_by_id('input_1')
# log.send_keys('macgrzelak')
# pas = self.driver.find_element_by_id('input_2')
# pas.send_keys('03*29_Ps&bY')
# self.driver.find_element_by_css_selector('.credentials_input_submit').click()
# log = self.driver.find_element_by_id('Login:LoginScreen:LoginDV:username-inputEl')
# log.send_keys('macgrzelak')
# pas = self.driver.find_element_by_id('Login:LoginScreen:LoginDV:password-inputEl')
# pas.send_keys('03*29_Ps&bY')
# self.driver.find_element_by_id('Login:LoginScreen:LoginDV:submit').click()
# time.sleep(2)
# WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Konta']"))).click()
# time.sleep(3)








# np.set_printoptions(linewidth=2000)

import difflib


""" PZU """












# find_all(ocr, page_source)


# print([i for i in difflib.ndiff(soup.text, ocr)])
# tags = ['div', 'tr', 'td', 'table', 'form', 'tbody', 'input', 'a', 'span', 'id', 'img']






# for path in find_all('tbody', task):
#     if path:
#         png = cv2.imread(os.getcwd() + f'/screenshot.png')
#
#         ocr = ocr_text(png)
        # print(ocr)

# cv2.waitKey(0)



# photo = cv2.imread(os.getcwd() + "/screenshot.png",0)
# # img = cv2.medianBlur(photo,5)
# ret, thresh4 = cv2.threshold(photo, 127, 255, cv2.THRESH_TOZERO)
# # print(thresh4)
# # th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# #
# #
# #
# #
# plt.imshow(thresh4, 'gray')
# plt.axis("off")
# plt.show()










# photo_PIL = Image.open(os.getcwd() + f"/screenshot.png").convert('RGBA')
# arr = np.array(photo_PIL)

# print(arr.shape)
# print(arr)




# photo = in_out.imread(os.getcwd() + f"/screenshot.png")
#
#
# print(photo.shape)
# plt.imshow(photo)
# plt.show()

















"""Buttons"""
# buttons = driver.find_elements_by_xpath(".//form//input[@type='button']")
# for button in buttons:
#     print(button.text)

# driver.find_elements_by_css_selector('input[type=button])

"""Wyszukanie po tekście"""
# WebDriverWait(driver, 4).until(EC.element_to_be_clickable
#                                ((By.XPATH, f"//*[contains(text(), '{text}')]")))

