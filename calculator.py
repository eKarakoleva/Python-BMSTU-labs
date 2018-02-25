from tkinter import *
from tkinter.ttk import Button, Entry, Style


def set_text(text):
    entry.insert(END, text)
    return


def get_text():
    try:
        equ = entry.get()
        total = str(eval(equ))
        entry.delete(0,END)
        entry.insert(0,total)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def ten_to_five_int(number):
    dev_result = int(number)
    res_array = []
    while int(dev_result) >= 5:
        res = dev_result % 5
        dev_result = dev_result // 5
        res_array.append(str(res))
    res_array.append(str(dev_result))
    total = list(reversed(res_array))
    return total


def ten_to_five():
    try:
        number = entry.get()
        if ("." not in number):
            total = ten_to_five_int(number)
            total = "".join(total)
            entry.delete(0, END)
            entry.insert(0, total)
        else:
            all_parts = number.split(".")
            work_value = float("0."+all_parts[1])
            res_array = []
            i=7
            while i > 0:
                mult = work_value*5
                temp = mult%1
                res_array.append(str(int(mult)))
                work_value = temp
                i-=1

            total_whole_part = ten_to_five_int(all_parts[0])
            total_whole_part = "".join(total_whole_part)
            total_after_dot = "".join(res_array)
            total_after_dot = float("0."+ total_after_dot)
            entry.delete(0, END)
            entry.insert(0, total_after_dot + int(total_whole_part))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def five_to_ten_int(number,count_1):
    res = 0
    count = count_1
    for i in number:
        res += (int(i) * (5 ** count))
        count -= 1
    return res


def five_to_ten():
    try:
        number = entry.get()
        invalid = {"6", "7", "8","9"}
        input = set(list(number))

        if(not bool(invalid&input)):
            if ("." not in number):
                res = five_to_ten_int(number,len(number))
                entry.delete(0, END)
                entry.insert(0, res)
            else:
                number = number.split(".")
                res_whole_part = five_to_ten_int(number[0],len(number[0])-1)
                res_after_dot = five_to_ten_int(number[1],-1)

                final = res_whole_part+res_after_dot
                entry.delete(0, END)
                entry.insert(0, final)
        else:
            entry.delete(0, END)
            entry.insert(0, "Error...wrong system")
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, END)


def clear_last():
    entry.delete(len(entry.get()) - 1, END)


def info():
    top = Toplevel()
    top.title("About this application...")
    text = "Hello, it's me!\nElena Karakoleva\nBauman MSTU"

    msg = Message(top, text=text , pady = 10)
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

self = Tk()
menubar = Menu(self)
commandmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Commands", menu=commandmenu)
commandmenu.add_command(label="+", command=lambda:set_text("+"))
commandmenu.add_command(label="-", command=lambda:set_text("-"))
commandmenu.add_command(label="*", command=lambda:set_text("*"))
commandmenu.add_command(label="/", command=lambda:set_text("/"))
commandmenu.add_command(label="Cls", command=lambda:clear())
commandmenu.add_command(label="Cls_last", command=lambda:clear_last())
commandmenu.add_separator()
commandmenu.add_command(label="Exit", command=self.quit)

systemmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Systems", menu=systemmenu)
systemmenu.add_command(label="10->5", command=lambda:ten_to_five())
systemmenu.add_command(label="5->10", command=lambda:five_to_ten())

info_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=info_menu)
info_menu.add_command(label="Elena Karakoleva \nBauman MSTU")

self.config(menu=menubar)

Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

entry = Entry(self)
entry.grid(row=0, columnspan=4, sticky=W + E)
cls = Button(self, text="Cls", command=lambda:clear())
cls.grid(row=1, column=0)
bck = Button(self, text="Cls_last",command=lambda:clear_last())
bck.grid(row=1, column=1)
lbl = Button(self)
lbl.grid(row=1, column=2)
clo = Button(self, text="")
clo.grid(row=1, column=3)
sev = Button(self, text="1", command=lambda:set_text("1"))
sev.grid(row=2, column=0)
eig = Button(self, text="2", command=lambda:set_text("2"))
eig.grid(row=2, column=1)
nin = Button(self, text="3", command=lambda:set_text("3"))
nin.grid(row=2, column=2)
div = Button(self, text="/", command=lambda:set_text("/"))
div.grid(row=2, column=3)

fou = Button(self, text="4", command=lambda:set_text("4"))
fou.grid(row=3, column=0)
fiv = Button(self, text="5", command=lambda:set_text("5"))
fiv.grid(row=3, column=1)
six = Button(self, text="6", command=lambda:set_text("6"))
six.grid(row=3, column=2)
mul = Button(self, text="*", command=lambda:set_text("*"))
mul.grid(row=3, column=3)

one = Button(self, text="7", command=lambda:set_text("7"))
one.grid(row=4, column=0)
two = Button(self, text="8", command=lambda:set_text("8"))
two.grid(row=4, column=1)
thr = Button(self, text="9", command=lambda:set_text("9"))
thr.grid(row=4, column=2)
mns = Button(self, text="-", command=lambda:set_text("-"))
mns.grid(row=4, column=3)

zer = Button(self, text="0", command=lambda:set_text("0"))
zer.grid(row=5, column=0)
dot = Button(self, text=".", command=lambda:set_text("."))
dot.grid(row=5, column=1)
equ = Button(self, text="=", command=lambda:get_text())
equ.grid(row=5, column=2)
pls = Button(self, text="+", command=lambda:set_text("+"))
pls.grid(row=5, column=3)

ten_five = Button(self, text="10->5",command=lambda:ten_to_five())
ten_five.grid(row=6, column=0)
dot = Button(self, text="5->10", command=lambda:five_to_ten())
dot.grid(row=6, column=1)
equ = Button(self, text="Info", command=lambda:info())
equ.grid(row=6, column=2)

self.mainloop()
