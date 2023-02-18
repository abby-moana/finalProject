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
    openNote.write(text)
    openNote.close()


def openNote():
    note = filedialog.askopenfile(mode="r", filetypes=[("text files", "*.txt")])
    if note is not None:
        content = note.read()
        entry.insert(INSERT, content)


def clearNote():
    entry.delete(1.0, END)


def newNote():
    root.title("Untitled - Notepad")
    entry.delete(1.0, END)


b1 = Button(root, text="Save", command=saveNote, bg="#99d18f")
b1.place(x=10, y=10)

b2 = Button(root, text="New", command=newNote, bg="#99d18f")
b2.place(x=55, y=10)

b3 = Button(root, text="Open", command=openNote, bg="#99d18f")
b3.place(x=105, y=10)

b4 = Button(root, text="Clear", command=clearNote, bg="#99d18f")
b4.place(x=155, y=10)

b5 = Button(root, text="Exit", command=exit, bg="#99d18f")
b4.place(x=205, y=10)

entry = Text(root, height=33, width=58, bg="#99d18f", wrap=WORD, font=("courier", 12))
