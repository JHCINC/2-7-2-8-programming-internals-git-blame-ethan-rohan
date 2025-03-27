import curses
#defines stdscr as initial screen
stdscr = curses.initscr()
#defines main using stdscr (Standard Screen)
def main(stdscr):
    #clears the terminal
    stdscr.clear()
    #adds the Hello World string to the terminal
    stdscr.addstr(0,0, "Hello World!")
    stdscr.refresh()
#Closes the tui loop (lets the code run)
if __name__ == "__main__":
    curses.wrapper(main)