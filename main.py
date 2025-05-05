#---------TK IMPORTS---------
import tkinter as tk
from tkinter import *
#---------FUNCTION IMPORTS---------

#from src.Notes import __init__ as note_ops
#command=note_ops.create_new_note
#---------FUNCTIONS-----------

def transparent():
    menubar.destroy()
    contents.destroy()
    men_collap.destroy()
    men_open.place(x=0,y=0)
def reopen():
    men_collap.place(x=150, y=0)
    menubar.pack(side=LEFT, fill=Y)
    men_open.destroy()
    
#---------MENU CONFIG---------
#This creates the main window/defines box for all gui elements.
box = tk.Tk()
#This defines the menu bar, Menu(box) means that the menu is in the box window.
menu = Menu(box)
box.config(menu=menu)
#Defines File as Menu(menu)
File = Menu(menu)
#Add cascade adds a menu tab, this tab is labeled as "File"
menu.add_cascade(label='File', menu=File)

#Submenu to File tab
#add_command adds a button under the File tab, An example of this is the New button for creating a new file
#command=Notes.init
File.add_command(label='New', )
File.add_command(label='Save')
File.add_command(label='Rename')
File.add_command(label='Open')
File.add_separator()
File.add_command(label="Close", command=box.quit)

#Defines Help as Menu(menu)
Help = Menu(menu)
#Add cascade adds a menu tab, this tab is labeled as "Help"
menu.add_cascade(label='Help', menu=Help)
Help.add_command(label='Source',)

#-----SCROLL BAR CONFIG-------

menubar = tk.Scrollbar(box)
menubar.pack(side=LEFT, fill=Y)
contents = Listbox(box, yscrollcommand=menubar.set)
for cont in range(100):
    contents.insert(END, '1')

contents.pack(side=LEFT, fill=BOTH)
menubar.config(command=contents.yview)

#---------MAIN CONFIG---------

#Window setup for the note app
#Background color
box.config(bg="blue")
#Title of the window that being "Note"
box.title("Note")
#Size of the window (Length & Width)
box.geometry("200x150")
#State of the window when created (Zoomed = Full Screen)
box.state("zoomed")


#----------CODE FOR VARIABLES---------

men_collap = tk.Button(box, text='-', width=1, height=1, command=transparent)
men_open = tk.Button(box, text='+', width=1, height=1, command=reopen)
#Text Box for type the note
text_box = tk.Text(box,width=140, height=50, bg="white", fg="black")

#Places all the variables in the box window using .place() e.g. labels, entry and text boxes 
text_box.place(x=250,y=85)
men_collap.place(x=150, y=0)

#Lets the Tk window be created (CLOSES THE LOOP)
box.mainloop()

