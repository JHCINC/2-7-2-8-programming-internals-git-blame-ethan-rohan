import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")
window.config(bg="#000099")
window.resizable(width=True,height=True)
window.title('Note Taking App')
window.state('zoomed')

qbox = tk.Entry(window,text="",font=("Arial",10),fg='#000099', bg="white", width=200)
test_box1 = tk.Label(window,text="This should be displaying text!",font=("Arial",20),fg="white", bg="#000099")

qbox.place(y=50, x=0)
test_box1.place(y=0,x=0)
window.mainloop()
