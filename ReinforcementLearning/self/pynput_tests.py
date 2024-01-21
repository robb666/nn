from pynput.keyboard import Controller
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
import pyperclip
import pyautogui
from time import sleep
import random


class Agent:

    def __init__(self):
        self.kb = Controller()
        self.mouse = MouseController()
        self.pol_chars = {'ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż'}

    def enter(self):
        self.kb.tap(Key.enter)

    def tab(self):
        self.kb.tap(Key.tab)
        # self.kb.Key.tab

    def tab_up(self):
        with self.kb.pressed(Key.shift):
            self.kb.tap(Key.tab)

    def up(self):
        self.kb(Key.up)

    def down(self):
        self.kb(Key.down)

    def back(self):
        with self.kb.pressed(Key.alt_l):
            self.kb.tap(Key.left)

    def forth(self):
        with self.kb.pressed(Key.alt_l):
            self.kb.tap(Key.right)

    def esc(self):
        self.kb.tap(Key.esc)

    def close_tab(self):
        with self.kb.pressed(Key.ctrl):
            self.kb.tap('w')

    def copy_paste(self, var):
        pyperclip.copy(var)
        with self.kb.pressed(Key.ctrl):
            self.kb.tap('v')

    def type_randomly(self, txt):
        for letter in txt:
            if letter in self.pol_chars:
                pyperclip.copy(letter)
                with self.kb.pressed(Key.ctrl):
                    self.kb.tap('v')
            else:
                self.kb.tap(letter)
            sleep(random.uniform(.06, .29))

    def click(self):  # TODO how to click in tab
        self.mouse.click(Button.left)

    # TODO del method

    def wait_0(self):
        sleep(random.uniform(.05, .12))

    def wait_1(self):
        sleep(random.uniform(.9, 1.4))

    # def hotkey(self, *keys):
    #     with self.kb.pressed(keys[0]):
    #         for key in keys[1:]:
    #             self.kb.tap(key)


data = ['6062815954', 'robert.try12@gmail.com']

# sleep(4)
A = Agent()


A.copy_paste(data[0])

A.tab()
A.tab()

A.type_randomly(data[1])

A.tab()

A.type_randomly(data[1])

A.tab()
A.tab()

A.enter()

A.back()

sleep(3)

A.forth()





# for _ in range(20):
#     pyautogui.hotkey("ctrl", "shift", "j")
#     kb.press(Key.end)
#     sleep(1)






































































































































