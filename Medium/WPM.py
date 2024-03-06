import curses
from curses import wrapper
#standard output screen

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM.exe! Test your limits today")
    stdscr.addstr("\nPress any key to continue")
    stdscr.refresh()
    stdscr.getkey()
    
def wpm_test(stdscr):
    target = "Hello Test 1,2,3 and Success!"
    current_text = []
    
    while True:
        key = stdscr.getkey()
        if ord(key) == 27: #ord ASCII key representation 27 = Space
            break
        current_text.append(key)
        stdscr.clear()
        stdscr.addstr(0,0,target)
        
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()
            
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    #key = stdscr.getkey() #wait for keyboard response
    start_screen(stdscr)
    wpm_test(stdscr)

    
wrapper(main)