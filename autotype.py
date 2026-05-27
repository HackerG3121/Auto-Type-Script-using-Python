# autotype.py
# Press ENTER anywhere to start auto typing from scriptfile.txt
# Works in places where copy-paste is blocked

import time
import keyboard
import pyautogui

FILE_NAME = "scriptfile.txt"

print("=== AUTO TYPE SCRIPT ===")
print("1. Open the target typing area")
print("2. Click inside the text field")
print("3. Press ENTER to start typing")
print("4. Press ESC anytime to stop\n")

# Read text file
with open(FILE_NAME, "r", encoding="utf-8") as file:
    content = file.read()

# Wait for ENTER key
keyboard.wait("enter")

print("Typing started in 3 seconds...")
time.sleep(3)

try:
    for char in content:
        if keyboard.is_pressed("esc"):
            print("Typing stopped.")
            break

        pyautogui.write(char)
        time.sleep(0.01)

    print("Finished typing.")

except KeyboardInterrupt:
    print("Stopped.")
