import pyautogui, time

time.sleep(5)

for x in range(10):
    with open("loveu.txt", "r") as l:
        for word in l:
            for chr in word:
                chr2 = chr.upper()
                pyautogui.write(chr2)
                pyautogui.press("enter")


