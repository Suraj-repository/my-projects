from tkinter import *


def click(event):
    global scr
    text = event.widget.cget("text")
    if text == "=":
        if scr.get().isdigit():
            int(scr.get())
        else:
            try:
                value = eval(screen.get())
            except:
                value = "Error"

            scr.set(value)
            screen.update()

    elif text == "C":
        scr.set("")
        screen.update()
    else:
        scr.set(scr.get() + text)
        screen.update()


root = Tk()
root.geometry("546x672")
root.title("Calculator by Hacker Hunter")
root.minsize(546, 672)
root.configure("skyblue")

scr = StringVar()
scr.set("")
screen = Entry(root, textvar=scr, font=("consolas", 40, "bold"))
screen.pack(fill=X, ipadx=8, padx=5, pady=20)
f = Frame(root, bg="black")
b = Button(f, text="1", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="2", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="3", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="4", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")

b = Button(f, text="5", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="6", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="7", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")

b = Button(f, text="9", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="0", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="+", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="-", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="/", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="*", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="%", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="C", font="consolas 40 bold", padx=28, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text=".", font="consolas 40 bold", padx=20, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="00", font="consolas 40 bold", padx=14, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="**", font="consolas 40 bold", padx=14, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="=", font="consolas 40 bold", padx=20, fg='red')
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
