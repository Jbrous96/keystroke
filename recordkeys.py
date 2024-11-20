from pynput.keyboard import Key, Listener
import datetime
import threading
import os
 
# Set up the text file
txt_file = "keystrokes.txt"
stop_flag = threading.Event()
 
def on_press(key):
    """
    Logs each key press to a text file with a timestamp.
 
    Args:
        key: The key that was pressed.
    """
    with open(txt_file, "a", encoding="utf-8") as f:
        if hasattr(key, "char"):
            f.write(f"{datetime.datetime.now()}: {key.char}\n")
        else:
            f.write(f"{datetime.datetime.now()}: {key}\n")
    if stop_flag.is_set():
        return False  # Stop the listener
 
def monitor_input():
    """
    Prompts the user to start and stop monitoring, and to exit the program.
    """
    input("Press Enter to start monitoring...\n")
 
    print("Monitoring keystrokes...\n")
 
    input("Press Enter to stop...\n")
 
    print("Saving log to:")
    print(f"- {os.getcwd()}/{txt_file}\n")
    stop_flag.set()
 
    print("Keystrokes saved to:")
    print(f"- {os.path.abspath(txt_file)}\n")
 
    input("Press Enter to exit...\n")
 
# Create a listener thread
listener_thread = threading.Thread(target=Listener(on_press=on_press).start)
 
# Start the listener thread
listener_thread.start()
 
# Monitor user input
monitor_input()
 
# Wait for the listener thread to finish
listener_thread.join()
 
print("Program exited... Goodbye!")
 
