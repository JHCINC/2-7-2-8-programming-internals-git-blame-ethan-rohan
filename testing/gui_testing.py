#---------TK IMPORTS---------
import tkinter as tk
from tkinter import *
#---------FUCTION IMPORTS---------

#TO BE ADDED

#---------CONFIG---------
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
File.add_command(label='New')
File.add_command(label='Rename')
File.add_command(label='Open')
File.add_separator()
File.add_command(label="Close", command=box.quit)
#Window setup for the note app
#Background color
box.config(bg="#000099")
#Title of the window that being "Note"
box.title("Note")
#Size of the window (Length & Width)
box.geometry("200x150")
#State of the window when created (Zoomed = Full Screen)
box.state("zoomed")


#----------CODE FOR VARIABLES---------
#Variables for the Tk window
#This variable is a text box to input the title of the note
input_title = tk.Entry(box, width=20,bg="white", fg="black")

#This is a label for the input box to help people understand what the box does
label_title = tk.Label(box, text="Name your note here:", width=20,bg="#000099", fg="white")

#Text Box for type the note
text_box = tk.Text(box,width=140, height=50, bg="white", fg="black")

#Places all the variables for labels, entry and text boxes in the box window using .place()
input_title.place(x=250,y=25)
label_title.place(x=225,y=0)
text_box.place(x=250,y=85)


#Lets the Tk window be created (CLOSES THE LOOP)
box.mainloop()

