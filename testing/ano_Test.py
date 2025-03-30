#Imports the curses module (Text User Interface MODULE)
import curses
#Defines stdscr = (Standard Screen)
stdscr = curses.initscr()

def main(stdscr):
    #defines color pair for text i.e. text color black, highlight color magenta
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_RED, curses.COLOR_BLACK)
    #Clears Terminal
    stdscr.clear() 
    #prints/adds the "Hello, I am using Curses!" 
    #The two numbers represent the y and x values of the text (0,0 == y,x)
    stdscr.addstr(0,0, "Hello, This is the testing document for this note taking app! ", curses.color_pair(1))
    stdscr.addstr(2,0, "Press the [1] to see the commands!", curses.color_pair(3))   
    #Refreshes everthing
    stdscr.refresh()
    while True:
        #Key = get key press
        key = stdscr.getch()
       
    
if __name__ == "__main__":
    curses.wrapper(main)