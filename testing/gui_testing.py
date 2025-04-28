#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

main = tk.Tk()
#note window
box_width = tk.Entry(main, width=50)
box_width.pack()

#Lets the Tk window be created
main.mainloop()
