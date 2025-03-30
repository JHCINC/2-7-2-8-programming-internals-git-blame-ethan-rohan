import curses
#defines stdscr as initial screen
stdscr = curses.initscr()
#defines main using stdscr (Standard Screen)
def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_BLACK)
    #clears the terminal
    stdscr.clear()
    #adds the Hello World string to the terminal
    stdscr.addstr(0,0, "Hello World!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()
#Closes the tui loop (lets the code run)
if __name__ == "__main__":
    curses.wrapper(main)
