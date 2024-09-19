import tkinter

root = tkinter.Tk()
root.geometry("500x500")
root.title("Time Calculator")
time = 48


def to_time(time):
    a = str(time // 4)
    b = str(15 * (time % 4))
    if len(a) < 2:
        a = " " + a
    if len(b) < 2:
        b = "0" + b
    return a + ":" + b


def ph():
    global time
    time += 4
    tl.config(text=to_time(time))


def mh():
    global time
    time -= 4
    tl.config(text=to_time(time))


def pm():
    global time
    time += 1
    tl.config(text=to_time(time))


def mm():
    global time
    time -= 1
    tl.config(text=to_time(time))


plhb = tkinter.Button(root, text="Plus 1 h", command=ph)
minhb = tkinter.Button(root, text="Minus 1 h", command=mh)

plmb = tkinter.Button(root, text="Plus 15 minutes", command=pm)
minmb = tkinter.Button(root, text="Minus 15 minutes", command=mm)

tl = tkinter.Label(root, text=to_time(time))

plhb.pack()
minhb.pack()
plmb.pack()
minmb.pack()
tl.pack()

root.mainloop()
