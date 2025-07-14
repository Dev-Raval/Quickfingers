import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3))
    stdscr.addstr(2, 0, f"WPM: {wpm}", curses.color_pair(4))

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Green
        if char != correct_char:
            color = curses.color_pair(2)  # Red
        stdscr.addstr(0, i, char, color)


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr, target_text):
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True)
    wpm = 0

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27: 
            exit()

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) 

    start_screen(stdscr)

    while True:
        target_text = load_text()
        wpm_test(stdscr, target_text)

        stdscr.addstr(4, 0, "✅ You completed the line!", curses.color_pair(1))
        stdscr.addstr(5, 0, "Do you want to continue? (Y/N): ", curses.color_pair(4))
        stdscr.refresh()

        key = stdscr.getkey()
        if key.lower() != 'y':
            stdscr.addstr(6, 0, "👋 Exiting the test. Thank you!", curses.color_pair(3))
            stdscr.refresh()
            time.sleep(2)
            break


wrapper(main)
