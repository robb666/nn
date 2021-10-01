import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import re
import time
import pandas as pd
from skimage import io as in_out
import matplotlib.pyplot as plt
import webp
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
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  # koniecznie -headless przy cronie

    def __init__(self, url: str, tasks: list, personal_data: dict):
        self.url = url
        self.tasks = tasks
        self.personal_data = personal_data
        self.driver.get(url)

        # self.body = requests.get(url).text  # html content
        # self.cv2 = cv2

    # def get_url(self):
    #     self.driver.get(self.url)

    def find_id(self, element):
        self.locator = self.driver.find_element_by_id(element)
        return self.locator

    def find_css(self, element):
        self.locator = self.driver.find_element_by_css_selector(element)
        return self.locator

    def find_class(self, element, n):
        self.locator = self.driver.find_elements_by_class_name(element)[n]
        return self.locator

    def find_xpath(self, element):
        self.locator = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, element)))
        return self.locator

    def send_keys(self, keys):
        self.locator.send_keys(keys)

    def write(self, text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    def press_key(self, key):
        actions = ActionChains(self.driver)
        actions.send_keys(key)
        actions.perform()

    # def _tag_visible(self, element):
    #     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
    #         return False
    #     if isinstance(element, Comment):
    #         return False
    #     return True
    #
    # def bs4_text(self, body):
    #     soup = BeautifulSoup(body, features="lxml")
    #     texts = soup.findAll(text=True)
    #     visible_texts = filter(self._tag_visible, texts)
    #     return u" ".join(t + '\n' for t in visible_texts)
    #
    # def driver_text(self):
    #     element = self.driver.find_element_by_xpath('//*')
    #     body = element.get_attribute('innerHTML')
    #     return self.bs4_text(body)

    def driver_text(self):
        # WebDriverWait(self.driver, 9).until(EC.visibility_of_element_located((By.XPATH, "/html/body")))
        return self.driver.find_element_by_xpath("/html/body").text

    def screen_shot(self):
        return self.driver.save_screenshot(f"screenshot.png")

    # # @staticmethod
    # def image_manipulation(self):
    #     png = cv2.imread(os.getcwd() + f'/screenshot.png')
    #     self.grey = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
    #     return self.grey

    # # @staticmethod
    # def ocr_text(self):
    #     self.ocr_excluded_items = []
    #     self.ocr = []
    #     ocr_raw = pytesseract.image_to_string(self.grey, lang='pol').split()
    #     self.to_replace = ('Nr', 'rej.', 'H', 'w', 'ic', 'c', 'u', 'Ś', 'E', 'v', 'V',
    #                        'p', 'T', 'ZŁ', '-MM-dd', 'E#', '.')
    #
    #     for raw in ocr_raw:
    #         if raw not in self.to_replace:
    #             self.ocr_excluded_items.append(raw)
    #
    #     for word in self.ocr_excluded_items:
    #         no_meta = re.sub(r'[)\]"|=_,*?©—-]|[0-9]', '', word)
    #         self.ocr.append(no_meta)
    #         self.ocr = list(filter(None, self.ocr))
    #
    #     return self.ocr

    def task_execution(self):
        while tasks:
            phrase = next(iter(tasks))
            visible_text = self.driver_text()
            if phrase == '*':
                self.form_fill()
            elif phrase := re.search(phrase, visible_text, re.I):  # Make case insensitive.
                re_phrase = phrase.group()
                try:
                    self.driver.find_element_by_xpath(f"//*[contains(text(), '{re_phrase}')]").click()
                except 1:
                    self.driver.find_element_by_xpath(f"//*[@class='bigButton' and contains(., '{re_phrase}')]").click()
                except 2:
                    self.driver.find_element_by_xpath(f"//*[@class='policy-name' and contains(text(), '{re_phrase}')]").click()

            tasks.pop(0)

    def form_fill(self):
        visible_text = self.driver_text()
        for k, v in personal_data.items():
            if (key := re.search(k, visible_text, re.I)) and k != '*':  # ??
                re_k = key.group()
                self.driver.find_element_by_xpath(f"//*[contains(text(), '{re_k}')]/following::input[1]").send_keys(v)

    # def wysiwyg(self):
    #     popped_items = []
    #     for i, ocr_txt in enumerate(self.ocr):
    #         print('!ocr: ', self.ocr, ocr_txt)
    #         print('!page_source: ', self.page_source)
    #         # if ocr_txt := re.search(re.escape(ocr_txt), self.next_page_source, re.I):
    #         # ocr_token = ocr_txt.group()
    #         print(ocr_txt)
    #         # try:
    #         WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH,
    #                                                        f"//*[contains(text(), '{ocr_txt}')]"))).click()
    #
    #         row = WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.CLASS_NAME, f"row"))).text
    #         print(row)
    #         """Nie uzupełnia formularza"""
    #         # self.form_fill()
    #         time.sleep(1.5)
    #         self.screen_shot()
    #         popped_items.append(self.ocr.pop(i))
    #         print(popped_items, '\n')
    #         # except:
    #         WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH,
    #                                                                             "//*[text()='Pulpit']"))).click()


url = 'https://everest.pzu.pl/pc/PolicyCenter.do'

tasks = ['pzu auto']

personal_data = {'Term public ID': '45',
                 'Numer polisy': '523654845',
                 'nazwisko': 'Grzelak',
                 'Imię': 'Robert',
                 'pesel': '82082407038'
                 }

location = "/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/Agent baza/Login_Hasło.xlsx"

pd.options.display.max_rows = 80
pd.options.display.max_columns = 10
pd.set_option("expand_frame_repr", False)
ws = pd.read_excel(location, index_col=None, na_values=['NA'], usecols="B:G")
df = pd.DataFrame(ws).head(80)

log = df.iloc[43, 4]
h = df.iloc[43, 5]

bot = BoT(url, tasks, personal_data)

bot.find_id('input_1').send_keys(log)
bot.find_id('input_2').send_keys(h)
bot.find_css('.credentials_input_submit').click()
bot.find_id('Login:LoginScreen:LoginDV:username-inputEl').send_keys(log)
bot.find_id('Login:LoginScreen:LoginDV:password-inputEl').send_keys(h)
bot.find_id('Login:LoginScreen:LoginDV:submit').click()
time.sleep(2)

bot.find_class('policy-icon', 1).click()


# bot.write('82082407038')
# bot.press_key(Keys.RETURN)
bot.task_execution()
# # bot.driver_text()
# # bot.form_fill()
#
#
# # bot.sleep(3)
# #
# # bot.page_source()
# # bot.screen_shot()
# # bot.image_manipulation()
# # bot.ocr_text()
# # # print(ocr)
# #
# #
# # # bot.task_execution()
# # # bot.form_fill()
