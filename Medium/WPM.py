import curses
from curses import wrapper
#standard output screen
def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.addstr("Welcome to WPM.exe! Test your limits today", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey() #getch() concept from C++
    

    
wrapper(main)