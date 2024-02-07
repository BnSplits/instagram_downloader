import json
from time import sleep
import pyautogui
import clipboard
import os
import pyperclip

#ceci est un test
# sleep(5)
# pyautogui.hotkey('ctrl','c')
# link = pyperclip.paste()

# os.system(f"echo '{link},' >> ./links.txt")
with open('db.json') as f:
    data = json.load(f)

print(data["mint"]["1920x1080"])