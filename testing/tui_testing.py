#Imports the curses module (Text User Interface MODULE)
import curses
#Defines stdscr = (Standard Screen)
stdscr = curses.initscr()

def main(stdscr):
    #defines color pair for text i.e. text color black, highlight color magenta
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_YELLOW, curses.COLOR_BLACK)
    #Clears Terminal
    stdscr.clear() 
    #prints/adds the "Hello, I am using Curses!" 
    #The two numbers represent the y and x values of the text (0,0 == y,x)
    stdscr.addstr(0,0, "Hello, This is the testing document for this note taking app! ", curses.color_pair(1))
    stdscr.addstr(2,0, "Press the [1] to see the commands!", curses.color_pair(3))   
    #Refreshes everthing
    stdscr.refresh()
    #This while loop checks of the "l" key to be pressed and then changes the beginning of the text to HELLO1
    while True:
        #Key = get key press
        key = stdscr.getch()
        #if inputted key is == l
        if key == ord("1"):
            stdscr.clear()
            stdscr.addstr(0,0, "Here are the Commands:")
            stdscr.addstr(2,0, "Press [Shift+7] to Add a Note", curses.color_pair(3))
            stdscr.addstr(3,0, "Press [Shift+8] to Delete a Note", curses.color_pair(4))
            stdscr.addstr(4,0, "Press [Shift+9] to View Previous Notes", curses.color_pair(5))
        else:
            #If 1 is not pressed then pass (Does Nothing)
            pass
    
        
#Runs the TUI/Closes the loop i.e lets the code for the TUI run.
if __name__ == "__main__":
    curses.wrapper(main)