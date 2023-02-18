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
