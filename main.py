import pyautogui, time 
# import msvcrt
# import scriptcontext
from pynput.keyboard import Key, Listener

run = True

def on_press(key):
    global run
    print('{0} pressed'.format(key))
    if key == Key.esc:
        run = False
        # Stop listener
        return False

listener = Listener(on_press=on_press)

listener.start()

time.sleep(2)  

print(pyautogui.size()) 

# pyautogui.moveTo(400, 400, duration = 1)  
# pyautogui.click(400, 400)

only_keyboard = False
only_mouse = True
no_click = True
steps = 800

if only_keyboard == True:
    count = 0
    command = "down"
    while(run):
        if (count < steps):
            time.sleep(1)  
            pyautogui.typewrite([command], 1)
            count = count+1
        else:
            if (command == "up"):
                command = "down"
            else:
                command = "up"
                pass
            count = 0
elif only_mouse == True:
    import random
    while(run):
        x = random.randint(550, 600)
        y = random.randint(550, 600)
        time.sleep(4)
        pyautogui.moveTo(x, y, duration = 1)