from inspect import getframeinfo
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(meters.get())
        foots.set(int(value * 3.2808399))
    except ValueError:
        pass

root = Tk()
root.title = "metric system guide for beginners 101 (easy)"
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


meters = StringVar()
meters_entry = ttk.Entry(mainframe, width = 7, textvariable=meters)
meters_entry.grid(column=2, row=1, sticky=(W,E))

foots = StringVar()
ttk.Label(mainframe, textvariable=foots).grid(column = 2, row = 2, sticky=(W,E))

ttk.Button(mainframe, text = "click me", command = calculate).grid(column=3, row=3, sticky=(W))
ttk.Label(mainframe, text = "foots").grid(column=3, row=2, sticky=(W))
ttk.Label(mainframe, text = "metres").grid(column=3, row=1, sticky=(W))
ttk.Label(mainframe, text = "is equivalent to").grid(column=1, row=2, sticky=(E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5 , pady=5)

meters_entry.focus()

root.bind("<Return>", calculate)
root.bind("<Escape>", exit)


#framewidth=mainframe.winfo_width()
#frameheight=mainframe.winfo_height()

#sizeofwindow = [framewidth, frameheight]
#print(sizeofwindow)

root.mainloop()

