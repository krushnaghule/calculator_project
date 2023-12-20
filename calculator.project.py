##### calculator project using python.
from tkinter import *
import click

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
              value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("350x900")
root.title("calculator by krushna")
# root.wm_iconbitmap("1.ico")
root.configure(background="grey")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipady=8, padx=10, pady=10)

f = Frame(root, bg="grey")
b = Button(f,text="9", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="8", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="7", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f,text="6", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="5", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="4", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f,text="3", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="2", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="1", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f,text="0", padx=2, pady=3,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="-", padx=2, pady=3,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="*", padx=2, pady=3,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f,text="/", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="%", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="=", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f,text="c", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="+", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="^", padx=1, pady=2,font="lucida 35 bold")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()








