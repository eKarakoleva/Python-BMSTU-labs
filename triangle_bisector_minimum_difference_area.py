'''
Program to find triangle (on a plane of dots)
which have a minimum difference between areas
of triangles made by one of the bisectors (min angle)
'''

from math import sqrt,degrees, acos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
import matplotlib
from tkinter import *
matplotlib.use("TkAgg")


def AddBtnClicked():
    try:
        x = float(xEntry.get())
        y = float(yEntry.get())
    except:
        messagebox.showerror("Error ", "You have to write x and y")
    else:
        point = "{}; {}".format(xEntry.get(), yEntry.get())
        yEntry.delete('0', END)
        xEntry.delete('0', END)
        if point not in pointsListBox.get("0", "end"):
            pointsListBox.insert("end", point)


def find_area(a, b, c):
    p = round((a + b + c) / 2, 5)
    area = (p * (p - a) * (p - b) * (p - c))
    if area > 0:
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        area = round(area, 5)
        return area
    else:
        return 0.0


def find_distance(x1, x2, y1, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def check_line(x1, x2, x3, y1, y2, y3):
    return (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1)


def readListBox(ListBox):
    points = [x.split("; ") for x in ListBox.get("0", "end")]
    x = []
    y = []
    for i in range(len(points)):
            x.append(int(points[i][0]))
            y.append(int(points[i][1]))
    return (x, y)


def find_bisector(x1,x2,y1,y2,side1,side2):
    constant = side1 / side2
    xd = (constant * x1 + x2) / (1 + constant)
    yd = (constant * y1 + y2) / (1 + constant)
    return (xd,yd)


def find_difference(x1,x2,y1,y2,x3,y3,side1,side2):
    xd, yd = find_bisector(x1,x2,y1,y2,side1,side2)

    bd = find_distance(xd, x2, yd, y2)
    dc = find_distance(x1, xd, y1, yd)
    ad = find_distance(xd, x3, yd, y3)

    area1 = find_area(bd, ad, side1)
    area2 = find_area(dc, ad, side2)
    return abs(area1 - area2)

# Составление всех возможных комбинаций с нахождением разницы площадей
def DrawBtnClicked():
    a.cla()
    x, y = readListBox(pointsListBox)
    min_difference = 0.0
    x_min = []
    y_min = []
    x_a = []
    y_a = []
    x_d = []
    y_d = []
    for ai in range(len(x)):
        for bi in range(ai+1, len(x)):
            for ci in range(bi+1, len(x)):
                if not check_line(x[ai], x[bi], x[ci], y[ai], y[bi], y[ci]):
                    ab = find_distance(x[bi], x[ai], y[bi], y[ai])
                    ac = find_distance(x[ci], x[ai], y[ci], y[ai])
                    bc = find_distance(x[ci], x[bi], y[ci], y[bi])

                    if ab < ac:
                        if ab < bc:
                            #ab
                            xd, yd = find_bisector(x[bi], x[ai], y[bi], y[ai], ac, bc)
                            difference = find_difference(x[bi], x[ai], y[bi], y[ai], x[ci], y[ci], ac, bc)
                            top = ci
                        else:
                            #bc
                            top = ai
                            xd, yd = find_bisector(x[ci], x[bi], y[ci], y[bi], ab, ac)
                            difference =find_difference(x[ci], x[bi], y[ci], y[bi], x[ai], y[ai], ab, ac)
                    else:
                        if ac < bc:
                            #ac
                            top = bi
                            xd, yd = find_bisector(x[ci], x[ai], y[ci], y[ai], ab, bc)
                            difference = find_difference(x[ci], x[ai], y[ci], y[ai], x[bi], y[bi], ab, bc)

                        else:
                            #bc
                            top = ai
                            xd, yd = find_bisector(x[ci], x[bi], y[ci], y[bi], ab, ac)
                            difference = find_difference(x[ci], x[bi], y[ci], y[bi], x[ai], y[ai], ab, ac)


                    if min_difference == 0.0:
                        min_difference = difference
                    if min_difference >= difference:
                        min_difference = difference
                        x_min = []
                        y_min = []
                        x_a = []
                        y_a = []
                        x_a.append(x[top])
                        y_a.append(y[top])
                        x_d = []
                        y_d = []
                        x_d.append(xd)
                        y_d.append(yd)
                        x_min.append(x[ai])
                        x_min.append(x[bi])
                        x_min.append(x[ci])
                        y_min.append(y[ai])
                        y_min.append(y[bi])
                        y_min.append(y[ci])

    if len(x) != 0 and len(x_min) != 0:
        x_min.append(x_min[0])
        y_min.append(y_min[0])
        a.scatter(x, y)
        a.plot([el for el in x_min], [el for el in y_min],"ro-")
        a.plot(x_a, y_a, "gx")
        a.plot(x_d, y_d, "gx")
        a.plot([x_a, x_d],[y_a, y_d], "go-")
        canvas.show()


        print('Разность площадей треугольников образуваны от бисектриса = {:.7f}'.format(min_difference))

    else:
        messagebox.showerror("Error ", "Все точки лежат на 1 прямой!")


root = Tk()

xLabel = Label(root, text="x:")
xEntry = Entry(root)

yLabel = Label(root, text="y:")
yEntry = Entry(root)
pointsListBox = Listbox(root)


xLabel.grid(column=1, row=0, sticky=E)
xEntry.grid(column=2, row=0)
yLabel.grid(column=1, row=1, sticky=E)
yEntry.grid(column=2, row=1)
pointsListBox.grid(column=2, row=3)

AddBtn = Button(root, text="Add point", command=AddBtnClicked)
AddBtn.grid(column=3, row=0, sticky=W)

DrawBtn = Button(root, text="Draw", command=DrawBtnClicked)
DrawBtn.grid(column=3, row=1, sticky=W)

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111, title="Graphic")
canvas = FigureCanvasTkAgg(f, master=root)  # plt.show()
canvas.get_tk_widget().grid(row=0, column=0, rowspan=100)

mainloop()
