import time
import glob
import sys
import os

import pyperclip
import pyautogui
import keyboard

from python_imagesearch.imagesearch import imagesearch

""" Class 'Operate of mouse'. """
class Mouse():
    def __init__(self):
        if keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed.')
            sys.exit()

    def click(self, a, b, t1):
        """ left click. """
        time.sleep(0.5)
        pyautogui.click(x=a, y=b)
        time.sleep(t1)
        if keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed.')
            sys.exit()

    def doubleClick(self, a, b, t1):
        """ double left click. """
        time.sleep(0.5)
        pyautogui.doubleClick(x=a, y=b)
        time.sleep(t1)
        if keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed.')
            sys.exit()


mouse = Mouse()

""" Class 'Looking for pictures'. """
class Imegesearch():

    def __init__(self):
        if keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed.')
            sys.exit()


    def pic(self, x, conf, func, t1):
        """ Main function 'looking for pictures'. """
        time.sleep(1)
        trial = 0
        path = f'sceenshots/screen_{x}.PNG'
        pos = imagesearch(path)
        time.sleep(1)
        if pos[0] != -1:
            print(f"I have founded '{x}', here is its coordinates: ", 'x = ', pos[0], '; ', 'y = ', pos[1])
            button = pyautogui.locateOnScreen(path, confidence=conf)
            time.sleep(1)
            if func == 1:
                pyautogui.click(button)
            elif func == 2:
                pyautogui.rightClick(button)
            elif func == 3:
                pyautogui.tripleClick(button)
            elif func == 4:
                pyautogui.doubleClick(button)
            time.sleep(1)
        elif pos[0] <= -1:
            if func == 1:
                while trial <= 2:
                    if trial == 0:
                        print(f'I can\'t find picture "{x}".')
                        trial = trial + 1
                        time.sleep(7)
                    elif trial == 1:
                        time.sleep(0.5)
                        path = f'sceenshots/screen_{x}.PNG'
                        pos = imagesearch(path)
                        if pos[0] != -1:
                            time.sleep(5)
                            print(f"I have founded '{x}', from trial 2 and conf = 0.99, here is its coordinates: ", 'x= ', pos[0], 'y= ', pos[1])
                            button = pyautogui.locateOnScreen(path, confidence=0.99)
                            pyautogui.click(button)
                            break
                        elif pos[0] <= -1:
                            print(f"I have not founded '{x}', from trial 2 and conf = 0.99--> bad practice")
                            trial = trial + 1
                            time.sleep(3)
                        print(f'The program will shut down, because i can\'t find picture "{x}" !')
                        sys.exit()
            elif func == 2:
                print('Can\'t see special word')
                pyautogui.scroll(-50)
                time.sleep(0.7)
                search.pic(x, conf, func, t1)
            elif func == 3:
                print('Can\'t see special word.')
                pyautogui.scroll(-50)
                time.sleep(1)
                search.pic(x, conf, func, t1)
            elif func == 4:
                pyautogui.scroll(-200)
                time.sleep(1)
                search.pic(x, conf, func, t1)
        elif keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed, The program will shut down.')
            sys.exit()
        else:
            print('The program shut down, something went wrong!')
        time.sleep(t1)

    def imgsearch_description(self, x, y, t1):
        """ Change description in Prom. """
        time.sleep(0.5)
        path = f'sceenshots/screen_{x}.PNG'
        path1 = f'sceenshots/screen_{y}.PNG'
        button = pyautogui.locateOnScreen(path, confidence=0.9)
        button1 = pyautogui.locateOnScreen(path1, confidence=0.95)
        pyautogui.mouseDown(button)
        time.sleep(0.5)
        pyautogui.moveTo(button1)
        time.sleep(0.5)
        pyautogui.mouseUp(button1)
        time.sleep(t1)


search = Imegesearch()

def tap_down():
    """ Several times push down. """
    time.sleep(0.5)
    pyautogui.scroll(-50)
    if keyboard.is_pressed('Esc') == True:
        print('Key "Esc" has been pressed.')
        sys.exit()

def deleting_foto():
    """ Delite '.JPG' in dir downloads. """
    dir = r'C:\Users\ADMIN\Downloads'
    extension = 'jpg'
    filelist = glob.glob(os.path.join(dir, '*.' + extension))
    for f in filelist:
        os.remove(f)
    time.sleep(0.5)

def write_txt():
    """ Copy discription from 'Tg' to '.txt'. """
    path_to_file = 'shoes_prom.txt'
    file0 = open(path_to_file, 'a', encoding = 'utf-8')
    file0.write(pyperclip.paste() + '\n\n\n\n\n\n\n\n\n\n\nNext card\n')
    file0.close()
    time.sleep(1)


itr = int(input('How much card, may i do? : '))
print()

search.pic(17, 0.9, 1, 1)

i = 0
while i < itr:
    search.pic(13, 0.9, 1, 1)
    search.pic(16, 0.9, 1, 1)

    for _ in range(21):
        tap_down()
    time.sleep(2)

    search.pic(4, 0.9, 2, 1)
    search.pic(10, 0.9, 1, 5)
    search.pic(4, 0.9, 2, 1)
    search.pic(15, 0.9, 1, 1)

    write_txt()

    pyautogui.scroll(-100)

    search.pic(14, 0.9, 1, 1)
    search.pic(24, 0.9, 1, 10)
    search.pic(25, 0.9, 1, 1)

    keyboard.write('python')
    time.sleep(5)

    search.pic(26, 0.95, 1, 7)
    search.pic(19, 0.9, 1, 1)
    search.pic(22, 0.9, 1, 5)
    search.pic(6, 0.9, 1, 1)

    search.imgsearch_description(7, 8, 2)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    search.pic(1, 0.9, 4, 2)
    search.pic(9, 0.9, 1, 5)

    mouse.doubleClick(566, 266, 5)

    search.pic(20, 0.9, 1, 3)
    search.pic(23, 0.9, 1, 3)

    pyautogui.scroll(2000)
    time.sleep(1)

    search.pic(11, 0.9, 1, 1)
    search.pic(12, 0.9, 1, 3)
    mouse.click(2071, 1191, 3)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.keyDown('enter')
    time.sleep(0.1)
    pyautogui.keyUp('enter')
    time.sleep(5)

    search.pic(6, 0.9, 1, 2)

    pyautogui.scroll(2000)

    search.pic(28, 0.9, 3, 1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    search.pic(23, 0.9, 1, 2)

    pyautogui.scroll(2000)

    search.pic(27, 0.9, 1, 1)
    pyautogui.hotkey('ctrl', 'a')

    copy_of_art = pyperclip.paste()
    copy_of_art = (copy_of_art.replace(': ', ' '))
    pyautogui.write(copy_of_art)
    time.sleep(1)

    search.pic(6, 0.9, 1, 2)
    pyautogui.scroll(2000)

    search.pic(5, 0.9, 3, 2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    search.pic(23, 0.9, 1, 2)
    pyautogui.scroll(2000)

    search.pic(3, 0.9, 1, 1)
    search.pic(2, 0.9, 4, 1)

    copy_of_art = pyperclip.paste()
    pyautogui.write(copy_of_art)
    time.sleep(1)

    mouse.click(1972, 195, 2)

    search.pic(18, 0.9, 1, 5.5)
    search.pic(18, 0.9, 1, 5.5)
    search.pic(21, 0.9, 1, 1)

    deleting_foto()

    i += 1
    print('I have been finished iterating №', i, '\n')
print('\nI have finished all iterating, you can check.')

