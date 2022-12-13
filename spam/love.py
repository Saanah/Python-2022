import pyautogui, time

time.sleep(5)

for x in range(10):
    with open("loveu.txt", "r") as l:
        for word in l:
            for chr in word:
                chrUpper = chr.upper()
                pyautogui.write(chrUpper)
                pyautogui.press("enter")


