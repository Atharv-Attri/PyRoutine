import pyautogui

def click(carray):
    file = carray
    with open(carray, 'r') as f:
        x = f.readlines()
    print(x) 
