import time
import sys
import os

import pyautogui
import keyboard
import glob

from python_imagesearch.imagesearch import imagesearch

""" Class 'Operaate of mouse'. """
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

    def rightClick(self, a, b, t1):
        """ right click. """
        time.sleep(0.5)
        pyautogui.rightClick(x=a, y=b)
        time.sleep(t1)
        if keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed.')
            sys.exit()

    def move(self, a, b, t1):
        """ move to click. """
        time.sleep(0.5)
        pyautogui.moveTo(x=a, y=b)
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
        path = f'screenshots_2/screen_{x}.PNG'
        pos = imagesearch(path)
        time.sleep(1)
        if pos[0] != -1:
            print(f"I have founded '{x}', here is its coordinates: ", 'x = ', pos[0], '; ', 'y = ', pos[1])
            button = pyautogui.locateOnScreen(path, confidence=conf)
            time.sleep(1)
            if func == 1:
                pyautogui.click(button)
            elif func == 2:
                pyautogui.mouseDown(button)
                time.sleep(0.5)
                pyautogui.moveTo(1913, 583, 1)
                time.sleep(3)
                pyautogui.mouseUp()
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
                        path = f'screenshots_2/screen_{x}.PNG'
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
                print('Can\'t do "Function 2"')
        elif keyboard.is_pressed('Esc') == True:
            print('Key "Esc" has been pressed, The program will shut down.')
            sys.exit()
        else:
            print('The program shut down, something went wrong!')
        time.sleep(t1)


search = Imegesearch()


def deleting_foto():
    """ Delite '.JPG' in dir downloads. """
    dir = r'C:\Users\ADMIN\Downloads'
    extension = 'jpg'
    filelist = glob.glob(os.path.join(dir, '*.' + extension))
    for f in filelist:
        os.remove(f)
    time.sleep(0.5)


print(' Не забудь --> должны быть открыты 2 вкладки(первая prom, вторая canva\n')
itr = int(input('How much card, may i do? : '))
print()

search.pic(121, 0.9, 1, 1)

i = 0
while i < itr:
    search.pic(101, 0.9, 1, 1)

    mouse.rightClick(714, 624, 1)

    search.pic(102, 0.9, 1, 1)

    mouse.click(407, 16, 10)  # Заходим в вторую карточку товара(усл-первая пром, третья канва)

    mouse.rightClick(1901, 982, 3) # наводим на главное фото и правой кнопкой

    search.pic(103, 0.9, 1, 4) # сохр
    search.pic(104, 0.9, 1, 4)  # сохр

    search.pic(100, 0.9, 1, 2) #канва
    search.pic(105, 0.9, 1, 2)
    search.pic(106, 0.9, 1, 4)

    mouse.doubleClick(557, 302, 8)

    mouse.click(151, 576, 3)

    search.pic(107, 0.9, 1, 1)
    search.pic(108, 0.9, 1, 1)
    search.pic(109, 0.9, 1, 1)
    search.pic(110, 0.9, 1, 1)
    search.pic(111, 0.9, 1, 1)
    search.pic(112, 0.9, 1, 1)
    search.pic(122, 0.9, 1, 5)

    mouse.click(407, 16, 4)  # вторая вкладка прома

    search.pic(113, 0.9, 1, 1)

    pyautogui.scroll(2000)

    for _ in range(7):
        mouse.click(2145, 1276, 1)

    search.pic(115, 0.9, 1, 5)

    mouse.doubleClick(557, 302, 8)  # первое фото
    search.pic(113, 0.9, 1, 1)

    search.pic(116, 0.9, 2, 1)
    search.pic(117, 0.9, 1, 1)
    search.pic(118, 0.9, 1, 1)

    mouse.click(706, 27, 2)  # закрыть вторую вкладку

    search.pic(101, 0.9, 1, 1)

    mouse.click(600, 617, 2)  # ставим галочку

    search.pic(119, 0.9, 1, 1)
    search.pic(120, 0.9, 1, 1)
    search.pic(118, 0.9, 1, 1)
    time.sleep(4)
    search.pic(118, 0.9, 1, 1)

    deleting_foto()

    i += 1
    print('I have been finished iterating №', i, '\n')
print('\nI have finished all iterating, you can check.')
