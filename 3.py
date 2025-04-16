import pyautogui
import time

# Start from 1
counter = 1

while True:
    pyautogui.write(str(counter))  # Convert the number to a string
    pyautogui.press('enter')  # Simulate pressing Enter
    counter += 1  # Increment the counter
    time.sleep(0.3)  # Pause for 0.3 seconds