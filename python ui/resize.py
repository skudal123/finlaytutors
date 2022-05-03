from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)

namelabel = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=False)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N,E,S,W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,W,S,E))
namelabel.grid(column=3, row=0, columnspan=2, sticky=(N,W), padx=10)
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), padx=10, pady=10)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0,weight=1)
content.columnconfigure(1,weight=1)
content.columnconfigure(2,weight=1)
content.columnconfigure(3,weight=1)
content.columnconfigure(4,weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()