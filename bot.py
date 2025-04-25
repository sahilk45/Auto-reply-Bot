import pyautogui
import time
import pyperclip

pyautogui.click(1430,1053)
time.sleep(1)

pyautogui.moveTo(486,451)
pyautogui.dragTo(562,944, duration=1,button= "left")

pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click(1842,79)

text= pyperclip.paste()
print(text)