import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Welcome to WPM.exe! Test your limits today", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()
    

    
wrapper(main)