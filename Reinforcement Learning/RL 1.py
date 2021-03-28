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


"""Sprawdza logowanie"""
def pzu_log(driver):
    driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')
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

    # return driver


def find_all(tag, tasks):
    phrase = {phrase.text for phrase in soup.findAll(tag) if not re.search('[\xa0\n]', phrase.text)}
    print(phrase)
    print(tasks)

    for i, task in enumerate(tasks):
        for link in phrase:

            if link not in ('', None, 'NoneType', 'None') and re.search(task, link, re.I):
                print(link)
                time.sleep(1)
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{link}']"))).click()
                WebDriverWait(driver, 4).until(EC.visibility_of_all_elements_located)
                time.sleep(1)

                driver.save_screenshot(f"screenshot.png")

                tasks.pop(i)
                find_all(tag, tasks)

                # photo = in_out.imread(os.getcwd() + f"/screenshot.png")
                # plt.imshow(photo)
                # plt.show()
                # print(photo.shape)
                # pdf = wi(filename=photo, resolution=250)
                # return scr
                # break

            # webp.save_image(scr, 'image.webp', quality=50)
            # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Ofert')]"))).click()



def ocr_text(png):
    text_ocr = pytesseract.image_to_string(png, lang='pol')

    return text_ocr



# np.set_printoptions(linewidth=2000)



""" PZU """
options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
pzu_log(driver)

soup = BeautifulSoup(driver.page_source, features="lxml")

tags = ['div', 'tr', 'td', 'table', 'form', 'tbody', 'input', 'a', 'span', 'id', 'img']

task = ['konta', 'transakcje', 'podmioty']

find_all('span', task)


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

