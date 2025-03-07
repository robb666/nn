from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import time
import re
# import cv2
import numpy as np


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')
#
# print(Dog.__mro__)

# https://www.programiz.com/python-programming/methods/built-in/super

company_tasks = [
                 'wyszukiwanie',
                 'podmiotu',
                 '*',
                 'zukaj',
                 'nowy podmiot',
                 'firma',
                 'dane adresowe',
                 '**',
                 {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
                 {'xpath': "(//*[@class='x-grid-checkcolumn'])[2]"},
                 'dane kontaktowe',
                 '**',
                 'dane dodatkowe',
                 '**',
                 'zapisz',
                 # 'zapisz',
                 'kcje',
                 'Utwórz Konto firmowe',
                 'zapisz',
                 ]

calc_tasks = [
                {'xpath': "(//*[contains(text(), 'Pojazd')])[1]"},
                'pojazd',
                '*',
]


company_tasks.clear()
company_tasks.extend(calc_tasks)


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


frd = vehicle_data['Data pierwszej rejestracji'].split('.')
frd = frd[-1] + frd[-2] + frd[-3]
vehicle_data['Data pierwszej rejestracji'] = frd


print(vehicle_data)






# data = {'Term public ID': '45',
#         'Numer polisy': '523654845',
#         'nazwisko': 'Grzelak',
#         'Imię': 'Robert',
#         'pesel': '71073141349',  # 92082407084
#         'kod pocztowy': '90-441',
#         'poczta': 'Łódź',
#         'województwo': 'MAZOWIECKIE',
#         'miejscowość': 'Łódź',
#         'ulica': 'Wólczańska',
#         'Numer budynku': '7a',
#         'Numer lokalu': '10'
#         }
#
# for i in data:
#         print(data[i])



# def _tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
#
#
# def page_text(body):
#     soup = BeautifulSoup(body, features="lxml")
#     texts = soup.findAll(text=True)
#     visible_texts = filter(_tag_visible, texts)
#
#     return u" ".join(t.strip() for t in visible_texts)
#
#
#
# r = requests.get('http://media4web.pl/').text
#
# print(page_text(r))








# """Nagranie pulpitu"""
#
# # display screen resolution, get it from your OS settings
# SCREEN_SIZE = (1920, 1080)
# # define the codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # create the video write object
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
#
#
# while True:
#     # make a screenshot
#     img = pyautogui.screenshot()
#     # convert these pixels to a proper numpy array to work with OpenCV
#     frame = np.array(img)
#     # convert colors from BGR to RGB
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # write the frame
#     out.write(frame)
#     # show the frame
#     cv2.imshow("screenshot", frame)
#     # if the user clicks q, it exits
#     if cv2.waitKey(1) == ord("q"):
#         break
#
# # make sure everything is closed when exited
# cv2.destroyAllWindows()
# out.release()
#
# for i in range(200):
#     # make a screenshot
#     img = pyautogui.screenshot()
#     # the rest of the code...






# arr = ['CTZA', 'DZ', 'Konta', None, 'Polisy', 'Podmioty', 'Wyszukiwanie', 'Zespół', 'Reporrowanie', 'Administracja', 'osx-pc-o-', 'Wiadomości', 'PZUWiem', 'PZUSA', 'WITAJ', 'MACIEJ', 'PESEL/REGON', 'Nazwisko/Nazwa', 'Oferta/Polisa', 'ZĄ', 'Everest', 'Zadania', 'Kema', 'SZYBKA', 'SPRZEDAŻ', 'BUDŻET', 'ZNIŻEK', 'MOJA', 'PROWIZJA', 'GOTÓWKA', 'DO', 'WPŁATY', 'oferty', 'Polisy', 'Wykorzystane:', 'Pozostało:', ')', '', '/', '', 'Transakcje', 'pozopała:', 'oBudżet', '', 'Kolejki', 'Ś', 'Rozliczenia', 'Plany', 'prowizyjne', 'OFWCA', 'u', 'u', 'Budżet', 'zniżek', 'Promokody', 'Moje', 'raporty', 'Szybkie', 'wyszukiwanie', 'ZALEGŁE', 'ó', 'ZADANIA', 'POLISY', 'DO', 'ZADANIA', 'KTÓRE', 'MOJE', 'WNIOSKI', 'Dokumenty', 'organizacji', 'WZNOWIENIA', 'NOWE', 'OFERTY', 'BY', 'OPŁACENIA', 'LECIŁEM', 'PRZYPISANE', 'DO', '', '', '', '', 'B', '', '', '', '', '', 'Wersja', 'zplikacji:', '--', ':']
#
# ocr = list(filter(None, arr))
# print(ocr)
#
#
#
# print('Konta|'.replace('|', ''))


# options = Options()
# options.add_argument('--window-size=2220,1080')
# driver = webdriver.Chrome(options=options)
#
# driver.get('https://everest.pzu.pl/pc/PolicyCenter.do')
# log = driver.find_element_by_id('input_1')
# log.send_keys('macgrzelak')
# pas = driver.find_element_by_id('input_2')
# pas.send_keys('03*29_Ps&bY')
# driver.find_element_by_css_selector('.credentials_input_submit').click()
# log = driver.find_element_by_id('Login:LoginScreen:LoginDV:username-inputEl')
# log.send_keys('macgrzelak')
# pas = driver.find_element_by_id('Login:LoginScreen:LoginDV:password-inputEl')
# pas.send_keys('03*29_Ps&bY')
# driver.find_element_by_id('Login:LoginScreen:LoginDV:submit').click()
# # time.sleep(2)
# # WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Konta']"))).click()
# time.sleep(3)
#
#
# tasks = ['konta', 'transakcje', 'podmioty', 'edytuj podmiot']
# personal_data = {'imię': 'robert', 'nazwisko': 'grzelak', 'pesel': '82082407038'}
#
#
#
# for phrase in tasks:
#     # for phrase in tasks:
#     print(phrase)
#     if phrase not in ('\n', '', ' ') and re.search(phrase, page_source, re.I):
#         print(phrase)
#         try:
#             WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
#                                                               f"//*[contains(text(), '{phrase.title()}')]"))).click()
#
#             WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
#                                                     f"//*[contains(@type, 'text') and @role='textbox']"))).send_keys('Robert')
#
#
#
#         except Exception as e:
#             print(f'{e} - exception!')
#             WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,
#                                                                             f"//*[text()='Konta']"))).click()









