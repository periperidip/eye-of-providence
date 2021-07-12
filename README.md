# The Eye of Providence

<p align = "middle">
<img src="artifacts/the-eye.PNG" alt="The Eye of Providence" width="250">
</p>


The Eye of Providence or the "All Seeing Eye" is a security exploration project which attempts to create a System-wide Keylogger for logging a target's keystrokes, storing them in a text file and reporting the keylog back to the attacker. The keylogger aims to hide itself from the common eye and rather execute in the background, disguising itself as a Windows program/process.

## Why 'Eye of Providence'

Quoting from [Wikipedia](https://en.wikipedia.org/wiki/Eye_of_Providence):

> The Eye of Providence (or the all-seeing eye of God) is
> a symbol that depicts an eye, often enclosed in a
> triangle and surrounded by rays of light or Glory, meant
> to represent divine providence, whereby the eye of God
> watches over humanity.

The name suggests that one is always being watched, no matter what they do or where they hide. Hence, this is why I named this keylogger 'The Eye of Providence' since the victim, blissfully unaware, is being surveilled, all their actions being recorded.

## How It Works

The keylogger is written in Python [3.9.6](https://www.python.org/downloads/release/python-396/) and uses the `pynput` [library](https://pynput.readthedocs.io/en/latest/) to record the user input. The benefit of `pynput` is that it by default listens to the keyboard input throughout the system, across all threads and processes, something which pushed me away from using the Windows API which requires setting up Hooks and call a new DLL to monitor system-wide keyboard input.

The keylogger stores the input in a text file in a prettier format which is easy to comprehend.

## Run

To run EOP, the following resources are necessary:

1. Python 3.x
2. `pynput`
3. `pyinstaller`<sup>*</sup>

<sup>*</sup>Not needed to run EOP but to create a functioning Windows executable (EXE).

### Windows

To install (2) and (3):

```powershell
pip install pynput
pip install pyinstaller
```

Now to run EOP via the command line:

```powershell
python .\main.py
```

EOP starts without any prompt on the terminal and can be exited by pressing the `ESC` key.

To create an EXE, we use `pyinstaller`, a [package](https://www.pyinstaller.org/) to create a standalone executable. Due to [this](https://github.com/moses-palmer/pynput/issues/312) issue (which is not fixed as of version 1.7.3) the command to create an executable is as follows:

```powershell
pyinstaller -F `
--hidden-import "pynput.keyboard._win32" `
--hidden-import "pynput.mouse._win32" `
--icon "artifacts/generic-process.ico" `
--noconsole `
.\main.py
```

The `-F` option creates a single bundled EXE called `main.exe` in the `dist/` directory. The `--no-console` options does not pop-up a console when the EXE is started and thus the file executes in the background. Other `pyinstaller` options can be explored in the [Documentation](https://pyinstaller.readthedocs.io/en/stable/).

### Linux<sup>+</sup>

To install (2) and (3):

```zsh
pip3 install pynput
pip3 install pyinstaller
```

Now to run EOP via the command line:

```zsh
python3 .\main.py
```

EOP starts without any prompt on the terminal and can be exited by pressing the `ESC` key.

On Linux, an EXE can be created using:

```zsh
pyinstaller -F --icon "artifacts/generic-process.ico" main.py
```

Now, since EXEs cannot be directly executed on Linux, we can execute it via the command-line using:

```
./main.exe
```

<sup>+</sup>Untested on Linux as of date but this is most probably how it should work.

## Output

The keylog is recorded after every 12 keys pressed. The captured keylog is stored in a text file and is processed to eliminate the `Key.space`, `Key.escape` and `Key.shift` keywords and instead substitute their easily readable equivalents. The keylog cuts to a new line after every 75 characters.

When a specific Hotkey is pressed, the keylogger quits.