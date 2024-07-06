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

    def __init__(self, details):
        self.kb = Controller()
        self.mouse = MouseController()
        self.pol_chars = {'ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż'}
        self.action_space = ['enter', 'tab', 'tab_up', 'up', 'down', 'back', 'forth', 'esc', 'change_tab',  # 'close_tab',
                             'copy_paste', 'type_randomly', 'click_kb', 'mouse_right', 'mouse_left', 'mouse_down',
                             'mouse_up', 'click', 'delete', 'wait_0', 'wait_1']
        self.data = details

    def choose_and_execute_action(self):
        action_name = random.choice(self.action_space)
        print(action_name)
        action = getattr(self, action_name)
        if action_name in ['type_randomly', 'copy_paste']:
            action(random.choice(self.data))  # TODO <-- single detail
        else:
            action()

    def enter(self):
        self.kb.tap(Key.enter)

    def tab(self):
        self.kb.tap(Key.tab)

    def tab_up(self):
        with self.kb.pressed(Key.shift):
            self.kb.tap(Key.tab)

    def up(self):
        self.kb.tap(Key.up)

    def down(self):
        self.kb.tap(Key.down)

    def back(self):
        with self.kb.pressed(Key.alt_l):
            self.kb.tap(Key.left)

    def forth(self):
        with self.kb.pressed(Key.alt_l):
            self.kb.tap(Key.right)

    def esc(self):
        self.kb.tap(Key.esc)

    def change_tab(self):
        with self.kb.pressed(Key.ctrl):
            self.kb.tap(Key.tab)

    # def close_tab(self):
    #     with self.kb.pressed(Key.ctrl):
    #         self.kb.tap('w')

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

    def click_kb(self):
        self.kb.tap(Key.space)

    def mouse_middle(self):
        pass  # Middle of the screen

    def mouse_right(self, x=20, y=0):
        self.mouse.move(x, y)

    def mouse_left(self, x=-20, y=0):
        self.mouse.move(x, y)

    def mouse_down(self, x=0, y=20):
        self.mouse.move(x, y)

    def mouse_up(self, x=0, y=-20):
        self.mouse.move(x, y)

    def click(self):
        self.mouse.click(Button.left, 1)

    def delete(self):
        with self.kb.pressed(Key.ctrl):
            self.kb.tap('a')
        self.kb.tap(Key.delete)

    def wait_0(self):
        sleep(random.uniform(.05, .12))

    def wait_1(self):
        sleep(random.uniform(.9, 1.4))

    # def hotkey(self, *keys):
    #     with self.kb.pressed(keys[0]):
    #         for key in keys[1:]:
    #             self.kb.tap(key)


data = ['6062815954', 'robert.try12@gmail.com']

sleep(4)


A = Agent(details=data)

for _ in range(10):
    A.choose_and_execute_action()
    sleep(.2)


# for _ in range(20):
#     pyautogui.hotkey("ctrl", "shift", "j")
#     kb.press(Key.end)
#     sleep(1)


