#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

box = tk.Tk()
menu = Menu(box)
box.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Rename')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label="Close", command=box.quit)
box.config(bg="#000099")
box.title("Note")
box.geometry("200x150")
box.state("zoomed")

input_title = tk.Entry(box, width=20,bg="white", fg="black")
label_title = tk.Label(box, text="Name your note here:", width=20,bg="#000099", fg="white")
print('I work!!')
#Placing labels and entry boxes on the window
input_title.place(x=250,y=25)
label_title.place(x=225,y=0)

#Text Box
box_width = tk.Text(box,width=140, height=50)
box_width.place(x=250,y=85)

#Lets the Tk window be created
box.mainloop()

