#imports for the tk window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
#The setup for the Tk window, e.g size state when opened and if resizable
window = tk.Tk()
window.geometry("400x400")
window.config(bg="#000099")
window.resizable(width=True,height=True)
window.title('Note Taking App')
window.state('zoomed')

#Testing fonts
my_font = Font(
    family = 'Times',
    size = 30,
    weight = 'bold',
    slant = 'roman',
    underline = 1,
    overstrike = 0
)
#Input box for note taking/data entry for notes during setup
note_name = tk.Entry(window,text="",font=(my_font,10),fg='#000099', bg="white", width=200)
#A simple label
test_box1 = tk.Label(window,text="Create your note!",font=(my_font,20),fg="white", bg="#000099")
#A button the currently does nothing
button1 = tk.Button(window,text="Press Me!", font=("Arial",20),fg='#000099',bg="blue")

#Placong all the variables on the Tk window
button1.place(y=80,x=12)
note_name.place(y=50, x=0)
test_box1.place(y=0,x=0)

#Lets the Tk window be created
window.mainloop()
