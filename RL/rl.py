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
import pyautogui
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
    options.add_argument('--window-size=3440,1440')
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
        self.locator = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, element)))
        return self.locator

    def find_css(self, element):
        self.locator = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        return self.locator

    def find_class(self, element):
        self.locator = self.driver.find_element_by_class_name(element)
        return self.locator

    def find_xpath(self, element):
        self.locator = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, element)))

        return self.locator

    def find_link(self, element):
        self.locator = self.driver.find_element_by_partial_link_text(element)
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

    # def __getitem__(self, item):
    #     self.tasks = tasks

    def task_execution(self):
        while tasks:
            phrase = next(iter(tasks))
            visible_text = self.driver_text()
            if phrase == '*':
                self.form_fill()

            elif phrase == '**':
                self.form_refill()

            elif isinstance(phrase, dict):
                print(phrase)
                if check := self.find_xpath(phrase.get('xpath')):
                    webdriver.ActionChains(self.driver).click_and_hold(check).perform()
                    webdriver.ActionChains(self.driver).release().perform()
                    time.sleep(.6)

            elif phrase := re.search(phrase, visible_text, re.I):  # Make case insensitive.
                re_phrase = phrase.group()
                try:
                    self.driver.find_element_by_xpath(f"//*[contains(text(), '{re_phrase}')]").click()
                except 1:
                    self.driver.find_element_by_xpath(f"//*[@class='bigButton' and contains(., '{re_phrase}')]").click()
                except 2:
                    print('except')
                    self.driver.find_element_by_xpath(f"//*[contains(., '{re_phrase}')]").click()
            tasks.pop(0)
            time.sleep(5)



    def form_fill(self):
        visible_text = self.driver_text()
        for k, v in data.items():
            if (key := re.search(k, visible_text, re.I)) and k != '*':
                re_k = key.group()
                self.driver.find_element_by_xpath(f"//*[contains(text(), '{re_k}')]/following::input[1]").send_keys(v)

    def form_refill(self):
        visible_text = self.driver_text()
        for k, v in data.items():
            if (key := re.search(k, visible_text, re.I)) and k not in ['*', '**']:
                re_k = key.group()
                box = self.driver.find_element_by_xpath(f"//*[contains(text(), '{re_k}')]/following::input[1]")
                if box.get_attribute('value') in ['', '<wybierz>']:
                    box.click()
                    box.send_keys(v)
                elif box.get_attribute('value') == '<Nieustalona>':
                    box.click()
                    box.send_keys(Keys.ARROW_UP)
                    box.send_keys(Keys.ARROW_UP)
                    box.send_keys(Keys.RETURN)
                    time.sleep(.5)


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
# url = 'https://everest.pzu.pl/my.policy'  # sandbox


data = {'Term public ID': '',
        'Numer polisy': '',
        'Imię': '',
        'nazwisko': '',
        'pesel': '',  # 99051222215
        'regon': '365897881',
        'kod pocztowy': '90-441',
        'poczta': 'Łódź',
        'województwo': 'Łódzkie'.upper(),
        'miejscowość': 'Łódź',
        'ulica': 'Kościuszki',
        'Numer budynku': '123',
        'Numer lokalu': '310',
        'E-mail główny': 'Klient odmówił',
        'Telefon główny': 'Klient odmówił'
        }

vehicle_data = {'DMC': '2315',
                 'Data pierwszej rejestracji': '15.03.2005',
                 'Import': 'tak',
                 'Kierownica po prawej stronie': 'NIE',
                 'Liczba miejsc': '5',
                 'Liczba współwłaścicieli': '1',
                 'Marka': 'BMW',
                 'Masa pojazdu': '1755',
                 'Moc': '200 kW',
                 'Model': '535 D',
                 'Numer VIN': 'WBANJ91030CR65131',
                 'Numer rejestracyjny': 'EL4C079',
                 'Paliwo': 'Olej napędowy',
                 'Pierwsza rejestracja w Polsce': '21.01.2011',
                 'Podrodzaj': 'kombi',
                 'Pojazd wyposażony w instalację LPG': 'NIE',
                 'Pojemność': '2993 cm3',
                 'Przebieg': '408484',
                 'Rodzaj': 'samochód osobowy',
                 'Rodzaj Podrodzaj': 'samochód osobowy kombi',
                 'Rodzaj pojazdu': 'Samochód osobowy',
                 'Rok produkcji': '2005',
                 'Specjalne użytkowanie': '-',
                 'Termin następnego bad. tech.': '08.06.2022',
                 'Ważność OC': '27.03.2022',
                 'Właściciel nr': '3',
                 'Ładowność pojazdu': '560'}


pezu_form = {'Numer rejestracyjny': vehicle_data.get('Numer rejestracyjny')}

tasks = ['wyszukiwanie',
         'podmiotu',
         '*',
         'zukaj',
         'nowy podmiot',
         'fizyczna',
         'dane adresowe',
         '**',
         {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
         {'xpath': "(//*[@class='x-grid-checkcolumn'])[3]"},
         'dane kontaktowe',
         '**',
         'zapisz',
         'zapisz',
         'kcje',
         'Utwórz Konto prywatne',
         'zapisz',
         ]

location = "/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/Agent baza/Login_Hasło.xlsx"

pd.options.display.max_rows = 80
pd.options.display.max_columns = 10
pd.set_option("expand_frame_repr", False)
ws = pd.read_excel(location, index_col=None, na_values=['NA'], usecols="B:G")
df = pd.DataFrame(ws).head(80)

log = df.iloc[43, 4]
h = df.iloc[43, 5]

bot = BoT(url, tasks, data)


# # sandbox
# bot.find_id('newSessionDIV').click()  # sanbox
# time.sleep(1)  # sanbox
# bot = BoT(url, tasks, data)
# time.sleep(1)  # sanbox
# # bot.find_css('body > center > p > a > span').click()
# time.sleep(1)  # sanbox

# Login
bot.find_id('input_1').send_keys(log)
bot.find_id('input_2').send_keys(h)
bot.find_css('.credentials_input_submit').click()
bot.find_id('Login:LoginScreen:LoginDV:username-inputEl').send_keys(log)
bot.find_id('Login:LoginScreen:LoginDV:password-inputEl').send_keys(h)
bot.find_id('Login:LoginScreen:LoginDV:submit').click()

# Check
bot.find_id('SalesSubmissionPzu:SalesSubmissionScreen:SalesSubmissionScreen:SmartSearchPzuPanelSet:smartSearchToolbarInput-inputEl')
id = data.get('pesel') if data.get('pesel') else data.get('regon')

bot.send_keys(id)

if len(id) == 11:
    locator = 'AccountFile_Summary:AccountFile_SummaryScreen:ContactData:AccountFileSummary_BasicInfoPzuPanelSet:lfProducts:1:bthLF'
else:
    locator = 'AccountFile_Summary:AccountFile_SummaryScreen:ContactData:AccountFileSummary_BasicInfoPzuPanelSet:lfProducts:0:bthLF'

try:
    bot.find_id('SalesSubmissionPzu:SalesSubmissionScreen:SalesSubmissionScreen:SmartSearchPzuPanelSet:smartSearchToolbarInput_Button').click()
    bot.find_id('DesktopClientsAccountsPzu:DesktopClientsAccountsScreen:0:AccountNumber').click()
    bot.find_id(locator).click()
    time.sleep(1.5)
    bot.find_id('escapeToEVE').click()
    bot.find_xpath("//button[@class='btn btn-primary' and text()='Tak']").click()

except:
    bot.task_execution()
    bot.find_css('#AccountFile_Summary\:AccountFile_SummaryScreen\:ContactData\:AccountFileSummary_BasicInfoPzuPanelSet\:lfProducts\:1\:bthLF > img').click()
    time.sleep(1.5)
    bot.find_id('escapeToEVE').click()
    bot.find_xpath("//button[@class='btn btn-primary' and text()='Tak']").click()






# bot.task_execution()
# to_click = bot.find_xpath('//img[@class="policy-icon" and text()=" PZU Auto "]')
# to_click = bot.find_link('/motorSaleLink.png')




# bot.write('82082407038')
# bot.press_key(Keys.RETURN)
# bot.task_execution()
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
