# ---------TK IMPORTS---------
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
box = tk.Tk()
# ---------FUNCTION IMPORTS---------
'''The function imports are commented becasue the are not recognising module: Classes, this is a error only in main.py '''
#from src.Notes import __init__ as note_ops
#command=note_ops.create_new_note

# ---------FUNCTIONS-----------
# This function makes the Listbox and Scrollbar disapear from the Tk window.
def transparent():
    menubar.pack_forget()
    contents.pack_forget()
# This function makes the Listbox and Scrollbar reappear in the Tk window.
def reopen():
    menubar.pack_configure(side=LEFT, fill=Y)
    contents.pack_configure(side = LEFT, fill= Y)
# This function makes it so the title can be editied by the end-user rather then be a constant set by the developer.
def title():
    tk_title = askstring('Setup', "Input your Title: ")
    showinfo('Your title is now {}'.format(tk_title))
    box.title(tk_title)
# Runs the fucntion
title()


#---------MENU CONFIG---------
# This creates the main window/defines box for all gui elements.
# This defines the menu bar, Menu(box) means that the menu is in the box window.
menu = Menu(box)
box.config(menu=menu)
# Defines File as Menu(menu)
File = Menu(menu)
# Add cascade adds a menu tab, this tab is labeled as "File"
menu.add_cascade(label='File', menu=File)

# add_command adds a button under the File tab, An example of this is the New button for creating a new file
# command=Notes.init
File.add_command(label='New', )
File.add_command(label='Save')
File.add_command(label='Rename', command=title)
File.add_command(label='Open')
File.add_separator()
File.add_command(label="Close", command=box.quit)

# Defines Help as Menu(menu)
Help = Menu(menu)
# Add cascade adds a menu tab, this tab is labeled as "Help"
menu.add_cascade(label='Help', menu=Help)
Help.add_command(label='Source',)

#-----SCROLL BAR CONFIG-------

menubar = tk.Scrollbar(box)
menubar.pack(side=LEFT, fill=Y)
contents = Listbox(box, yscrollcommand=menubar.set)
for cont in range(100):
    contents.insert(END, 1 + cont)
contents.pack(side=LEFT, fill=BOTH)
menubar.config(command=contents.yview)

# ---------MAIN CONFIG---------

# Window setup for the note app
# Background color
box.config(bg="blue")
# Title of the window that being "Note"
# Size of the window (Length & Width)
box.geometry("200x150")
# State of the window when created (Zoomed = Full Screen)
box.state("zoomed")


# ----------CODE FOR VARIABLES---------

men_collap = tk.Button(box, text='-', width=1, height=1, command=transparent)
men_open = tk.Button(box, text='+', width=1, height=1, command=reopen)
# Text Box for type the note
text_box = tk.Text(box,width=175, height=160, bg="white", fg="black")

# Places all the variables in the box window using .place() e.g. labels, entry and text boxes 
text_box.place(x=196,y=0)
men_collap.place(x=1425, y=0)
men_open.place(x=1425, y=28)
# Lets the Tk window be created (CLOSES THE LOOP)
box.mainloop()

