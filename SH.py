import time
import keyboard
import detectImage
import globalVariables


def start_stop():
    if globalVariables.start:
        print("Shop Helper: OFF")
        globalVariables.start = False
    else:
        print("Shop Helper: ON")
        globalVariables.start = True


def start_loop():
    while True:
        try:
            if globalVariables.start:
                detectImage.is_image_on_screen()

            time.sleep(0.1)
        except Exception as e:
            print(e)
            continue


keyboard.add_hotkey("'", start_stop)

start_loop()
