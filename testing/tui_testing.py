import curses
stdscr = curses.initscr()

def main(stdscr):
    #defines color pair for text i.e. text color black, highlight color magenta
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
    #Clears screen
    stdscr.clear() 
    #prints/adds the "Hello, I am using Curses!" 
    stdscr.addstr(0,0, "Hello, I am using Curses!", curses.color_pair(1))
    #refreshes everthing
    stdscr.refresh()
    #This while loop checks of the "l" key to be pressed and then changes the beginning of the text to HELLO1
    while True:
        key = stdscr.getch()
        if key == ord("l"):
            stdscr.addstr(0,0, "HELLO1", curses.color_pair(2))
        else:
            stdscr.addstr(0,0, "HELLO")
    
        
#Runs the TUI/Closes the loop
if __name__ == "__main__":
    curses.wrapper(main)