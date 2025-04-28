#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

main = tk.Tk()
box = tk.Tk()
#note window
title_name = tk.Entry(main, width=50)
print('i work!!')
title_name.pack()
#Text Box
box.title(title_name)
box_width = tk.Text(box, width=50, height=50)
box_width.pack()

#Lets the Tk window be created
box.mainloop()
