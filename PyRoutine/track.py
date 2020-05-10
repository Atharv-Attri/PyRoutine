import pyautogui
from pynput import keyboard
click_list = []
x = []
y = []
def on_press(key):
    try:
        if key.char == "c":
            # do something
            print("c")
            click_list.append(pyautogui.position())
            
        elif key.char == "v":
            # do something else
            return False  # Stop listener
    except AttributeError as ex:
        print(ex)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def get_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() # wait till listener will stop
    # other stuff        
    x = [i[0] for i in click_list]
    y = [i[1] for i in click_list]
    with open('clicklist.txt', 'w') as filehandle:
            for i in range(0,x.__len__()):
                filehandle.write(str(click_list[i])+"\n")
    return(0)

get_input()
#print([i[0] for i in click_list])
#x = [i[0] for i in click_list]
#y = [i[1] for i in click_list]
#for i in range(0, y.__len__()):
#    print(x[i])
#    print(y[i])
#    pyautogui.click(x[i], y[i])
