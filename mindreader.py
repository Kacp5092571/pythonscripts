from tkinter import messagebox
from tkinter import simpledialog
chosennumber = simpledialog.askstring('Mind Reader', 'Write a number.')
fullnum = ("Your number is" + " " + chosennumber)
messagebox.showinfo('Your number', fullnum)
