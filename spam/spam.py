import pyautogui, time
time.sleep(5)

for x in range(10):
    with open("loveu.txt", "r") as f:
        for line in f:
         pyautogui.typewrite(line.upper())
         pyautogui.press("enter") 