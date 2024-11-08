import pyperclip
import time
import os
import sys
import keyboard  # Library to listen for keypresses

# File where clipboard data will be saved
file_path = "paste.txt"


def save_to_file(text):
    with open(file_path, "a") as f:  # Append mode
        lineSpace = "\n"
        f.write(text + 3 * lineSpace)  # Add two newlines after each entry


def clear_file():
    """Clear the contents of the file."""
    with open(file_path, "w") as f:  # Write mode clears the file
        pass
    print("File cleared!")


def stop_program():
    """Stop the program."""
    global is_running
    is_running = False
    print("Program stopped!")


def create_key_listeners():
    """Listen for the Backspace key and clear the file when pressed."""
    keyboard.add_hotkey("backspace", clear_file)
    keyboard.add_hotkey("esc", stop_program)  # Wait for the Esc key to stop the program


def clipboard_listener():
    """Continuously monitor clipboard for changes."""
    print("Listening for clipboard changes...")
    previous_text = ""
    global is_running
    while is_running == True:
        try:
            current_text = pyperclip.paste()
            if (
                current_text != previous_text and current_text
            ):  # Check if new text is different
                save_to_file(current_text)
                print(f"New text detected")
                previous_text = current_text
            time.sleep(1)  # Poll every second
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)


if __name__ == "__main__":
    if not os.path.exists(file_path):
        open(file_path, "w").close()
    is_running = True
    create_key_listeners()
    clipboard_listener()
