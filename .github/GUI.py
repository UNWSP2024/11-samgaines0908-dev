#Author: Sam Gaines
#Date: 4/17/2026
#Title: GUI Window

import tkinter as tk

window=tk.Tk()
window.geometry("500x500")
saying = "To give anything less than your best is to sacrifice the gift-Pre"

label = tk.Label(window,text=saying, font=("Times New Roman", 25))
label.pack()

window.mainloop()