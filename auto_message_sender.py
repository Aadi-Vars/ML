import pyautogui
import time
time.sleep(5)
for i in range(5):
	pyautogui.typewrite("hello")
	pyautogui.press('enter')