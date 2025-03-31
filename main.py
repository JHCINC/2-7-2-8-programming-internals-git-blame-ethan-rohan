import curses
import datetime
#defines stdscr as initial screen
stdscr = curses.initscr()
date = str(datetime.datetime.now())
#defines main using stdscr (Standard Screen)
def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_RED, curses.COLOR_BLACK)
    #clears the terminal
    stdscr.clear()
    #adds the Hello World string to the terminal
    stdscr.addstr(0,0, "Thank You for using this Note Taking App!", curses.color_pair(1))
    stdscr.addstr(2,0, "Press the [1] to see the commands.", curses.color_pair(3)) 
    while True:
        key = stdscr.getch()

        if key == ord("1"):
            stdscr.clear()
            stdscr.addstr(0,0, "Here are the Commands:", date)
            stdscr.addstr(2,0, "Press [+] to Add a Note", curses.color_pair(6))
            stdscr.addstr(3,0, "Press [-] to Delete a Note", curses.color_pair(4))
            stdscr.addstr(4,0, "Press [Shift+9] to View Previous Notes", curses.color_pair(5))
            stdscr.addstr(6,0, "Press the [2] to go back to the main menu!", curses.color_pair(3))   
        elif key == ord("2"):
            stdscr.clear()
            stdscr.addstr(0,0, "Thank You for using this Note Taking App! ", curses.color_pair(1))
            stdscr.addstr(2,0, "Press the [1] to see the commands.", curses.color_pair(3))   
            #Refreshes everthing
            stdscr.refresh()
        elif key == ord('+'):
            curses.wrapper(main)

        else:
            #If 1 is not pressed then pass (Does Nothing)
            pass
#Closes the tui loop (lets the code run)
if __name__ == "__main__":
    curses.wrapper(main)
print(note)