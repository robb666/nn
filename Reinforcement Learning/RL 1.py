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

    def __init__(self, cv2):
        self.cv2 = cv2

    def pzu_log(self):
        self.driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')
        log = self.driver.find_element_by_id('input_1')
        log.send_keys('macgrzelak')
        pas = self.driver.find_element_by_id('input_2')
        pas.send_keys('03*29_Ps&bY')
        self.driver.find_element_by_css_selector('.credentials_input_submit').click()
        log = self.driver.find_element_by_id('Login:LoginScreen:LoginDV:username-inputEl')
        log.send_keys('macgrzelak')
        pas = self.driver.find_element_by_id('Login:LoginScreen:LoginDV:password-inputEl')
        pas.send_keys('03*29_Ps&bY')
        self.driver.find_element_by_id('Login:LoginScreen:LoginDV:submit').click()
        time.sleep(2)
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Konta']"))).click()
        time.sleep(3)
        return self.driver

    def page_source(self):
        soup = BeautifulSoup(self.driver.page_source, features="lxml")
        return soup.get_text()

    def screen_shot(self):
        return self.driver.save_screenshot(f"screenshot.png")

    def image_manipulation(self):
        png = cv2.imread(os.getcwd() + f'/screenshot.png')
        return cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)

    def ocr_text(self):
        return pytesseract.image_to_string(grey, lang='pol')

    def find_all(self, ocr, page_source):
        for phrase in ocr.split('\n'):
        # for phrase in tasks:
            # print(phrase)
            if phrase not in ('\n', '', ' ') and re.search(phrase, page_source, re.I):
                print(phrase)
                try:
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH,
                                                                    f"//*[contains(text(), '{phrase.title()}')]"))).click()
                except Exception as e:
                    print(f'{e} - exception!')
                    WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Konta']"))).click()


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


bot = BoT(cv2)
print(bot.__dict__)
bot.pzu_log()
page_source = bot.page_source()
bot.screen_shot()
grey = bot.image_manipulation()
ocr = bot.ocr_text()
bot.find_all(ocr, page_source)

















# np.set_printoptions(linewidth=2000)

import difflib


""" PZU """








tasks = ['konta', 'transakcje', 'podmioty', 'edytuj podmiot']



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

