from tkinter import *

root = Tk()

def callback(*args):
    print(sv.get())
    print(entry.get())

sv = StringVar()

sv.trace("w", callback)

entry = Entry(root, textvariable=sv)

entry.pack()

root.mainloop()