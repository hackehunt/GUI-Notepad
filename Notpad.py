from tkinter import *
import tkinter.messagebox as tmsg
import webbrowser
import gmail
import os
from tkinter.filedialog import *


# Basic tkinter setup
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      "Text Documents"])
    if file == "":
        file = None
    else:
        root.title(f"{os.path.basename(file)} - Hacker pad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def new():
    global file
    root.title("Untitled - Hacker pad")
    file = None
    textarea.delete(1.0, END)


def save():
    pass


def saveas():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            "Text Documents"])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
    # else:
    #     f = open(file, "w")
    #     f.write(textarea.get(1.0, END))
    #     f.close()


def copy():
    textarea.event_generate("<<Copy>>")


def cut():
    textarea.event_generate("<<Cut>>")


def paste():
    textarea.event_generate("<<Paste>>")


def about():
    tmsg.showinfo("Hacker pad", "Hacker pad is a text IDE created by Hacker Hunter on 06/03/2020")

def feed():
    webbrowser.open("mail.google.com")
    tmsg.showinfo("E-mail", "Send your feedback at princebarnwal69@gmail.com")

root = Tk()
root.title("Hacker pad")
root.geometry("500x400")
root.minsize(400, 300)
# Text area
textarea = Text(root, font="consolas 25 bold")
file = None
textarea.pack(fill=BOTH, expand=True)
# Creating our menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
# To open a new file
filemenu.add_command(label="New Project", command=new)
filemenu.add_separator()
# To open a existing file
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
# To save a file
# filemenu.add_command(label="Save", command=save)
# filemenu.add_separator()
# To save a file as user want
filemenu.add_command(label="Save as", command=saveas)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
# Edit menu
editmenu = Menu(menubar, tearoff=0)
# copy command
editmenu.add_command(label="Copy", command=copy)
editmenu.add_separator()
# Cut command
editmenu.add_command(label="Cut", command=cut)
editmenu.add_separator()
# Paste command
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
menubar.add_cascade(label="Edit", menu=editmenu)
# Editmenu ends
# Help menu
Exit = Menu(menubar, tearoff=0)
Exit.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="Exit", menu=Exit)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
# About Hackerpad
helpmenu.add_command(label="About Hackerpad", command=about)

# Send feedback
helpmenu.add_command(label="feedback", command=feed)

helpmenu.add_cascade(label="Help")
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
# Scroll bar
scroll = Scrollbar(textarea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)
root.mainloop()
