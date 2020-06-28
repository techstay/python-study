import pyautogui
import time

time.sleep(3)

# Windows计算器的按钮截图
five = '5.png'
eight = '8.png'
multiply = 'multiply.png'
equals = 'equals.png'

# 图片识别和点击的函数


def find_and_click(image):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(x, y)


# 执行5*8=
find_and_click(five)
find_and_click(multiply)
find_and_click(eight)
find_and_click(equals)
