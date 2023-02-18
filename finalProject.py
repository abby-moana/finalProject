from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg="pink")

icon = ImageTk.PhotoImage(Image.open("notepad.png"))
root.iconphoto(False, icon)

scrollbar = scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

def saveNote():
    openNote = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if openNote is None:
        return
    text = str(entry.get(1.0, END))
