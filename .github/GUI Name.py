#Author:
#Date: 4/17/2026
#Title: GUI Name Display

import tkinter as tk

def show_info():

    info_label.config(text="Sam Gaines. 838 Charlotte Dr ,Anoka, Minnesota ")

window = tk.Tk()
window.geometry("500x500")

info_label= tk.Label(window, text="", font=("Times New Roman", 15), justify="center")
info_label.pack()

show_button = tk.Button(window, text="Show Info", command=show_info)
show_button.pack()

quite_button = tk.Button(window, text="Quit", command=window.quit)
quite_button.pack()
window.mainloop()


