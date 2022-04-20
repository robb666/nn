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

# import pandas as pd
# import pyautogui
# from skimage import io as in_out
# import matplotlib.pyplot as plt
# import webp
# import os
# from PIL import Image
# from wand.image import Image as wi
# import pytesseract
# import io
# import cv2


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

    def __init__(self, tasks: list, personal_data: dict):
        self.tasks = tasks
        self.personal_data = personal_data
        # self.body = requests.get(url).text  # html content
        # self.cv2 = cv2

    def get_url(self, url):
        options = Options()
        options.add_argument('--window-size=1000, 1000')
        # options.add_argument('--headless')  # koniecznie -headless przy cronie
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)

    def find_id(self, element):
        self.locator = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, element)))
        return self.locator

    def find_css(self, element):
        self.locator = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        return self.locator

    def find_class(self, element):
        self.locator = self.driver.find_element_by_class_name(element)
        return self.locator

    def find_xpath(self, element):
        self.locator = WebDriverWait(self.driver, 9).until(EC.element_to_be_clickable((By.XPATH, element)))
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

    def ac_click(self, element):
        webdriver.ActionChains(self.driver).click_and_hold(element).perform()
        webdriver.ActionChains(self.driver).release().perform()

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


class specPezuBoT(BoT):
    def __init__(self, tasks, data):
        super().__init__(tasks, data)
        # self.tasks = tasks
        # self.data = data

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
            print(phrase)
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
                print(phrase)
                re_phrase = phrase.group()
                try:
                    if re_phrase == 'Nowy podmiot':
                        time.sleep(2.5)
                    self.find_xpath(f"//*[contains(text(), '{re_phrase}')]").click()
                except:
                    print('fackuop')
                    self.find_xpath(f"//*[@class='bigButton' and contains(., '{re_phrase}')]").click()
                # except:
                #     self.driver.find_element_by_xpath(f"//*[contains(., '{re_phrase}')]").click()
            tasks.pop(0)
            time.sleep(.5)

    def form_fill(self):
        visible_text = self.driver_text()
        print(visible_text)
        if 'Typ' in visible_text and 'pojazdu' not in visible_text:
            box_typ = self.find_xpath(f"//*[contains(text(), 'Typ')]/following::input[1]")
            if box_typ.get_attribute('value') != 'Firma' and data.get('regon'):
                self.write('Firma')
                box_typ.send_keys(Keys.TAB)
                time.sleep(.3)

        for k, v in data.items():
            if (key := re.search(k, visible_text, re.I)) and k != '*':
                re_k = key.group()
                self.find_xpath(f"//*[contains(text(), '{re_k}')]/following::input[1]").send_keys(v)
            else:
                pass

    def form_refill(self):
        visible_text = self.driver_text()
        for k, v in data.items():
            if (key := re.search(k, visible_text, re.I)) and k not in ['*', '**']:
                re_k = key.group()
                box = self.find_xpath(f"//*[contains(text(), '{re_k}')]/following::input[1]")
                if box.get_attribute('value') == '<wybierz>' and k == 'Znacznik podmiotu':
                    for _ in range(3):
                        box.send_keys(Keys.ARROW_UP)
                    box.send_keys(Keys.RETURN)
                    time.sleep(.5)
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




# # url = 'https://everest.pzu.pl/my.policy'  # sandbox
#
# personal_data = {'Data urodzenia': '26-01-1984',
#                  'Imię': 'Michał',
#                  'Kod pocztowy': '-',
#                  'Nazwisko': 'Piotrowicz',
#                  'PESEL': '82082407038'}
#
# company_data = {'Term public ID': '',
#                 'Numer polisy': '',
#                 'nazwa': 'AQUARID TRANS SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ',
#                 'regon': '382582078',
#                 'kod pocztowy': '37-700',
#                 'poczta': '37-700',
#                 'województwo': 'Podkarpackie'.upper(),
#                 'miejscowość': 'Przemyśl',
#                 'ulica': '3 MAJA',
#                 'Numer budynku': '8',
#                 'Numer lokalu': '',
#                 'E-mail główny': 'Klient odmówił',
#                 'Telefon główny': 'Klient odmówił',
#                 'Znacznik podmiotu': 'Pozostałe (niefinansowe)'
#                 }
#
# # vehicle_data = {'DMC': '2315',
# #                  'Data pierwszej rejestracji': '15.03.2005'.split('.')[-1] +
# #                                                '15.03.2005'.split('.')[-2] +
# #                                                '15.03.2005'.split('.')[-3],
# #                  'Import': 'tak',
# #                  'Kierownica po prawej stronie': 'NIE',
# #                  'Liczba miejsc': '5',
# #                  'Liczba współwłaścicieli': '1',
# #                  'Marka': 'BMW',
# #                  'Masa pojazdu': '1755',
# #                  'Moc': '200 kW',
# #                  'Model': '535 D',
# #                  'Numer VIN': 'WBANJ91030CR65131',
# #                  'Numer rejestracyjny': 'EL4C079',
# #                  'Paliwo': 'Olej napędowy',
# #                  'Pierwsza rejestracja w Polsce': '21.01.2011',
# #                  'Podrodzaj': 'kombi',
# #                  'Pojazd wyposażony w instalację LPG': 'NIE',
# #                  'Pojemność': '2993 cm3',
# #                  'Przebieg': '408484',
# #                  'Rodzaj': 'samochód osobowy',
# #                  'Rodzaj Podrodzaj': 'samochód osobowy kombi',
# #                  'Rodzaj pojazdu': 'Samochód osobowy',
# #                  'Rok produkcji': '2005',
# #                  'Specjalne użytkowanie': '-',
# #                  'Termin następnego bad. tech.': '08.06.2022',
# #                  'Ważność OC': '27.03.2022',
# #                  'Właściciel nr': '3',
# #                  'Ładowność pojazdu': '560'}
#
#
# vehicle_data = {'DMC': '1590',
#                 'Data pierwszej rejestracji': '20.02.2006'.split('.')[-1] +
#                                               '20.02.2006'.split('.')[-2] +
#                                               '20.02.2006'.split('.')[-3],
#                  'Import': 'nie',
#                  'Kierownica po prawej stronie': 'NIE',
#                  'Liczba miejsc': '5',
#                  'Liczba współwłaścicieli': '0',
#                  'Marka': 'FIAT',
#                  'Masa pojazdu': '1030',
#                  'Moc': '48 kW',
#                  'Model': 'PUNTO',
#                  'Numer VIN': 'ZFA19900001045125',
#                  'Numer rejestracyjny': 'WOS83815',
#                  'Paliwo': 'Gaz / benzyna',
#                  'Pierwsza rejestracja w Polsce': '20.02.2006',
#                  'Podrodzaj': 'wielozadaniowy',
#                  'Pojazd wyposażony w instalację LPG': 'TAK',
#                  'Pojemność': '1242 cm3',
#                  'Przebieg': '248601',
#                  'Rodzaj': 'samochód osobowy',
#                  'Rodzaj Podrodzaj': 'samochód osobowy wielozadaniowy',
#                  'Rodzaj pojazdu': 'Samochód osobowy',
#                  'Rok produkcji': '2006',
#                  'Specjalne użytkowanie': '-',
#                  'Termin następnego bad. tech.': '18.01.2022',
#                  'Ważność OC': 'Brak info',
#                  'Właściciel nr': '4',
#                  'Ładowność pojazdu': '560'}
#
# person_tasks = ['wyszukiwanie',
#                  'podmiotu',
#                  '*',
#                  'zukaj',
#                  'nowy podmiot',
#                  'fizyczna',
#                  'dane adresowe',
#                  '**',
#                  {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
#                  {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
#                  'dane kontaktowe',
#                  '**',
#                  'zapisz',
#                  'zapisz',
#                  'kcje',
#                  'Utwórz Konto prywatne',
#                  'zapisz',
#                 ]
#
# company_tasks = [
#                  'wyszukiwanie',
#                  'podmiotu',
#                  '*',
#                  'zukaj',
#                  'nowy podmiot',
#                  'firma',
#                  'dane adresowe',
#                  '**',
#                  {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
#                  {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
#                  'dane kontaktowe',
#                  '**',
#                  'dane dodatkowe',
#                  '**',
#                  'zapisz',
#                  'kcje',
#                  'Utwórz Konto firmowe',
#                  'zapisz',
#                  ]
#
#
# url = 'https://everest.pzu.pl/pc/PolicyCenter.do'
# location = "/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/Agent baza/Login_Hasło.xlsx"
#
#
# tasks = person_tasks if personal_data.get('PESEL') else company_tasks
# data = personal_data | vehicle_data if personal_data.get('PESEL') else company_data | vehicle_data
#
# bot = specPezuBoT(tasks, data)
#
#
# def login_pezu(location):
#     pd.options.display.max_rows = 80
#     pd.options.display.max_columns = 10
#     pd.set_option("expand_frame_repr", False)
#     ws = pd.read_excel(location, index_col=None, na_values=['NA'], usecols="B:G")
#     df = pd.DataFrame(ws).head(80)
#     # print(df)
#     log = df.iloc[30-2, 4]
#     h = df.iloc[30-2, 5]
#
#     # Login
#     bot.get_url(url)
#     bot.find_id('input_1').send_keys(log)
#     bot.find_id('input_2').send_keys(h)
#     bot.find_css('.credentials_input_submit').click()
#     bot.find_id('Login:LoginScreen:LoginDV:username-inputEl').send_keys(log)
#     bot.find_id('Login:LoginScreen:LoginDV:password-inputEl').send_keys(h)
#     bot.find_id('Login:LoginScreen:LoginDV:submit').click()
#
#
# def entity_check():
#     bot.find_id('SalesSubmissionPzu:SalesSubmissionScreen:SalesSubmissionScreen:SmartSearchPzuPanelSet:smartSearchToolbarInput-inputEl')
#     id = personal_data.get('PESEL') if personal_data.get('PESEL') else company_data.get('PESEL')
#
#     bot.send_keys(id)
#
#     if len(id) == 11:
#         locator = 'AccountFile_Summary:AccountFile_SummaryScreen:ContactData:AccountFileSummary_BasicInfoPzuPanelSet:lfProducts:1:bthLF'
#     else:
#         locator = 'AccountFile_Summary:AccountFile_SummaryScreen:ContactData:AccountFileSummary_BasicInfoPzuPanelSet:lfProducts:0:bthLF'
#     # Existing
#     try:
#         bot.find_id('SalesSubmissionPzu:SalesSubmissionScreen:SalesSubmissionScreen:SmartSearchPzuPanelSet:smartSearchToolbarInput_Button').click()
#         bot.find_id('DesktopClientsAccountsPzu:DesktopClientsAccountsScreen:0:AccountNumber').click()
#         time.sleep(1.5)
#         bot.find_id(locator).click()
#         time.sleep(1.5)
#
#         try:
#             bot.find_id('escapeToEVE').click()
#             bot.find_xpath("//button[@class='btn btn-primary' and text()='Tak']").click()
#         except:
#
#             bot.find_id(locator).click()
#             time.sleep(1.5)
#             bot.find_id('escapeToEVE').click()
#             bot.find_xpath("//button[@class='btn btn-primary' and text()='Tak']").click()
#
#         time.sleep(3)
#     # New
#     except:
#         bot.task_execution()
#         bot.find_id(locator).click()
#         time.sleep(2)
#         bot.find_id('escapeToEVE').click()
#         bot.find_xpath("//button[@class='btn btn-primary' and text()='Tak']").click()
#         time.sleep(3)
#
#
# def calc_start(vehicle_data):
#     bot.find_id('SaleSubmissionWizard:PmoVehicleId').click()
#     calc_tasks = ['*']
#     tasks.clear()
#     tasks.extend(calc_tasks)
#
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:RegistrationNo-inputEl').send_keys(vehicle_data['Numer rejestracyjny'])
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:VIN-inputEl').send_keys(vehicle_data['Numer VIN'])
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:FirstRegistrationDate-inputEl').send_keys(vehicle_data['Data pierwszej rejestracji'])
#     bot.press_key(Keys.TAB)
#     # Rok prod
#     # Rodzaj
#     # time.sleep(2)
#
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:Make-inputEl')
#     for _ in range(15):
#         bot.send_keys(Keys.BACK_SPACE)
#
#     # time.sleep(2)
#     bot.send_keys(vehicle_data['Marka'])
#     bot.press_key(Keys.TAB)
#
#
# def engine_ccm(vehicle_data):
#     engine_ccm = int(vehicle_data['Pojemność'].split()[0])
#
#     if engine_ccm < 1400:
#         engine_ccm = 'Poniżej 1400 ccm'
#     elif 1400 < engine_ccm < 1599:
#         engine_ccm = '1400 ccm - 1599 ccm'
#     elif 1600 < engine_ccm < 1799:
#         engine_ccm = '1600 ccm - 1799 ccm'
#     elif 1800 < engine_ccm < 1949:
#         engine_ccm = '1800 ccm - 1949 ccm'
#     elif 1950 < engine_ccm < 2099:
#         engine_ccm = '1950 ccm -  2099 ccm'
#     elif 2100 < engine_ccm < 2499:
#         engine_ccm = '2100 ccm -  2499 ccm'
#     else:
#         engine_ccm = 'Powyżej 2500 ccm'
#
#     time.sleep(.5)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:EngineSizeRange-inputEl')
#     for _ in range(15):
#         bot.send_keys(Keys.BACK_SPACE)
#     bot.send_keys(engine_ccm)
#     bot.press_key(Keys.TAB)
#
#
# def engine_type(vehicle_data):
#     fuel = vehicle_data['Paliwo']
#     if fuel == 'Benzyna' and fuel != 'HYBRID':
#         fuel = 'Benzyna'
#     elif fuel in ['Gaz / benzyna', 'benzyna, gaz']:
#         fuel = 'Benzyna i Gaz'
#     elif fuel in ['HYBRID', 'Hybryda benzyna-elektr.']:
#         fuel = 'Hybrydowy'
#     elif fuel == 'Olej napędowy':
#         fuel = 'Diesel'
#     else:
#         print('paliwo fuckup')
#
#     time.sleep(.5)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:FuelType-inputEl')
#     bot.send_keys(fuel)
#     # time.sleep(1)
#     bot.press_key(Keys.TAB)
#
#
# def model_pezu(vehicle_data):
#     # time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:Model-inputEl').click()
#     time.sleep(.2)
#     bot.write(f"{vehicle_data['Pojemność'].split()[0]}ccm, {vehicle_data['Moc'].replace(' ', '')}")
#     time.sleep(.2)
#     bot.press_key(Keys.RETURN)
#     time.sleep(.8)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:VehicleVersionPicker:SelectVehicleVersionPicker').click()
#     time.sleep(.4)
#     bot.find_id('VehicleVersionSelectPzuPopup:0:_Select').click()
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:Mileage-inputEl').send_keys(vehicle_data['Przebieg'])
#     lease = bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:IsLeased_false-boxLabelEl')
#     lease.click()
#
#
# def scope_pezu():
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehicleInformationPanelSet:Mileage-inputEl').click()
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehiclePzuCoverOptionPanelSet:PMOVehiclePzuCoverOptionInputSet:tah_PAPreselection-inputEl').click()
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehiclePzuCoverOptionPanelSet:PMOVehiclePzuCoverOptionInputSet:tah_WindscreenPreselection-inputEl').click()
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:SaleSubmissionVehicleDataPanelSet:PmoVehiclePzuCoverOptionPanelSet:PMOVehiclePzuCoverOptionInputSet:tah_CascoPreselection-inputEl').click()
#     time.sleep(1)
#     bot.find_id('SaleSubmissionWizard:SaleSubmissionInsuranceDataScreen:JobWizardToolbarButtonSet:QuoteOrReview-btnInnerEl').click()
#
#
# def run_pezu():
#     login_pezu(location)
#     entity_check()
#     calc_start(vehicle_data)
#     engine_ccm(vehicle_data)
#     engine_type(vehicle_data)
#     model_pezu(vehicle_data)
#     scope_pezu()
#
#
# run_pezu()
