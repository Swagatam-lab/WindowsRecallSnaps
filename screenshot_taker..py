import pyautogui
import time
import os
from datetime import datetime

def create_folder_for_today():
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join("screenshots", today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def take_screenshot(folder_path):
    timestamp = datetime.now().strftime("%H-%M-%S")
    filename = f"{timestamp}.png"
    filepath = os.path.join(folder_path, filename)
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"[✓] Screenshot saved at {filepath}")

def main():
    print("📸 Screenshot app started. Press Ctrl+C to stop.")
    while True:
        folder = create_folder_for_today()
        take_screenshot(folder)
        time.sleep(5)  # wait for 5 seconds

if __name__ == "__main__":
    main()
# This script will take a screenshot every 5 seconds and save it in a folder named with today's date.
# Make sure to have the 'pyautogui' library installed: pip install pyautogui
# Also, ensure that the script has permission to access the screen and save files in the current directory.
# To stop the script, you can use Ctrl+C in the terminal.