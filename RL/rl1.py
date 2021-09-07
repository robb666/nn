
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
from skimage import io as in_out
import matplotlib.pyplot as plt
# import webp
import os
from PIL import Image
from wand.image import Image as wi
import pytesseract
import io
import cv2


# print(pytesseract.get_tesseract_version())
# print(pytesseract.pytesseract)


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
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    def __init__(self, url: str, tasks: list, data: dict):
        self.url = url
        self.tasks = tasks
        self.data = data
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

    def find_all_xpath(self, element):
        self.locator = WebDriverWait(self.driver, 4).until(EC.presence_of_all_elements_located((By.XPATH, element)))
        return self.locator

    def send_keys(self, keys):
        self.locator.send_keys(keys)

    def page_source(self):
        self.page_source = BeautifulSoup(self.driver.page_source, features="lxml").get_text()
        return self.page_source

    def screen_shot(self):
        return self.driver.save_screenshot(f"screenshot.png")

    @staticmethod
    def write_txt(path, name, text):
        path = path if path.endswith('/') else path + '/'
        with open(path + name, 'w+') as f:
            f.write(f'{text}\n')

    # @staticmethod
    def image_manipulation(self):
        png = cv2.imread(os.getcwd() + f'/screenshot.png')
        self.grey = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
        return self.grey

    # @staticmethod
    def ocr_text(self):
        """!!!"""
        # nazwa = driver.find_element_by_xpath("(//div/h1)").text
        # dane = driver.find_element_by_xpath("(//div/h3)").text
        self.ocr_excluded_items = []
        self.ocr = []
        ocr_raw = pytesseract.image_to_string(self.grey, lang='pol').split()
        self.to_replace = ('Nr', 'rej.', 'H', 'w', 'ic', 'c', 'u', 'Ś', 'E', 'v', 'V',
                           'p', 'T', 'ZŁ', '-MM-dd', 'E#', '.')

        for raw in ocr_raw:
            if raw not in self.to_replace:
                self.ocr_excluded_items.append(raw)

        for word in self.ocr_excluded_items:
            no_meta = re.sub(r'[)\]"|=_,*?©—-]|[0-9]', '', word)
            self.ocr.append(no_meta)
            self.ocr = list(filter(None, self.ocr))

        return self.ocr

    def task_execution(self):
        for phrase in self.tasks:
            if phrase := re.search(phrase, self.driver.page_source, re.I):  # Make case insensitive.
                re_phrase = phrase.group()
                WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH,
                                                               f"//*[text()[contains(.,'{re_phrase}')]]"))).click()

    def form_fill(self):
        for k, v in self.data.items():
            # print('!page source: ' + self.next_page_source)
            if key := re.search(k, self.page_source, re.I):
                re_k = key.group()
                # print(re_k)
                try:
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                f"//*[contains(text(), '{re_k}')]/following::input[1]"))).send_keys(v)

                    """Dorobić klikniecie do przesłania formularza."""
                except:
                    print('Brak BOXa !')
                    pass

    def wysiwyg(self):
        popped_items = []
        for i, ocr_txt in enumerate(self.ocr):
            print('!ocr: ', self.ocr, ocr_txt)
            print('!page_source: ', self.page_source)
            # if ocr_txt := re.search(re.escape(ocr_txt), self.next_page_source, re.I):
            # ocr_token = ocr_txt.group()
            print(ocr_txt)
            # try:
            WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH,
                                                           f"//*[contains(text(), '{ocr_txt}')]"))).click()

            row = WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.CLASS_NAME, f"row"))).text
            print(row)
            """Nie uzupełnia formularza"""
            # self.form_fill()
            time.sleep(1.5)
            self.screen_shot()
            popped_items.append(self.ocr.pop(i))
            print(popped_items, '\n')
            # except:
            WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH,
                                                                                "//*[text()='Pulpit']"))).click()












# nazwa = bot.find_xpath("(//div/h1)").text
# dane = bot.find_xpath("(//div/h3)").text
# bot.page_source()
# bot.screen_shot()
# bot.image_manipulation()
# bot.ocr_text()
# print(ocr)


# bot.task_execution()
# bot.form_fill()
# bot.wysiwyg()






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

