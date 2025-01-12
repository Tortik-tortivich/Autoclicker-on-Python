#Вам нужно установить библеотеку keyboard и mouse/You need to install library keyboard and mouse.
import keyboard
import mouse
import time

isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Autoclicker off')
    else:
        isClicking = True
        print('Autoclicker onn')

#Вместо Alt + Z, вы можете поставить другую комбинацию клавиш/Instead of Alt + Z, you can use another key combination.
keyboard.add_hotkey('Alt + Z',set_clicker)

while True:
    if isClicking:
        #Если вам надо чтобы нажимала кнопку на клавиатуре,то пропишите keyboard.press_and_release('Название кнопки')/If you need to press a button on the keyboard, then write keyboard.press_and_release('Button name').
        mouse.double_click(button='left')
        #Вы можете поставить любое время на нажатие/You can set any time to press.
        time.sleep(0.01)
