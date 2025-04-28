#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


box = tk.Tk()
#seeing if i can make two windows at the same time

main = tk.Tk()
main.config(bg="#000099")
main.title("Name Your Note")
main.geometry("200x150")
input_title = tk.Entry(main, width=20,bg="white", fg="black")
print('i work!!')
input_title.place(x=10,y=7)


#Text Box
#box.title("hello")  #(f"{input_title}")
box.wait_window()
box_width = tk.Text(box, width=50, height=50)
box_width.pack()

#Lets the Tk window be created
box.mainloop()
main.mainloop()
