Ensure that you have the necessary permissions to run the script.    - This script monitors and logs keystrokes to a text file.

    - It uses the pynput library to listen for keyboard events and logs each keystroke with a timestamp.
    - The script prompts the user to start and stop monitoring, and to exit gracefully.
 
    - on_press(key):
        Logs each key press to a text file with a timestamp.
    - monitor_input():
        Prompts the user to start and stop monitoring, and to exit the program.
 
Requirements:
    - Python 3.x
    - Pynput Module (install using `pip install pynput`)
   
Usage:
    - Run the script using `python recordkeys.py`.
    - Follow the prompts in the terminal to start monitoring, stop monitoring, and exit the program.
 
Example Expected Output:
 
    2020-04-20 18:16:26.210462: Key.enter
    2020-04-20 18:16:35.858730: t
    2020-04-20 18:16:36.041972: e
    2020-04-20 18:16:36.265978: s
    2020-04-20 18:16:36.506444: t
    2020-04-20 18:16:37.178961: Key.space
    2020-04-20 18:16:37.686928: k
    2020-04-20 18:16:37.836686: e
    2020-04-20 18:16:38.111881: y
    2020-04-20 18:16:38.363728: s
    2020-04-20 18:16:38.565703: t
    2020-04-20 18:16:38.721222: r
    2020-04-20 18:16:39.167719: o
    2020-04-20 18:16:39.399612: k
    2020-04-20 18:16:39.618355: e
    2020-04-20 18:16:39.894371: Key.space
    2020-04-20 18:16:40.355300: r
    2020-04-20 18:16:40.572588: e
    2020-04-20 18:16:40.881969: c
    2020-04-20 18:16:41.117424: o
    2020-04-20 18:16:41.482916: r
    2020-04-20 18:16:41.766971: d
    2020-04-20 18:16:41.976781: e
    2020-04-20 18:16:42.208465: r
