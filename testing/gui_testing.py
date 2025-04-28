#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

main = tk.Tk()
box = tk.Tk()
#seeing if i can make two windows at the same time
while True:
    main.config(bg="#000099")
    main.title("Name Your Note")
    main.geometry("200x150")
    input_title = tk.Entry(main, width=20,bg="white", fg="black")
    print('i work!!')
    input_title.place(x=10,y=7)
    break
#Text Box
box.title(f"{input_title}")
box_width = tk.Text(box, width=50, height=50)
box_width.pack()

#Lets the Tk window be created
box.mainloop()
main.mainloop()
