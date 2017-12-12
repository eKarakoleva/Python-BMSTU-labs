'''
Program to find triangle (on a plane of dots)
which have a minimum difference between areas
of triangles made by one of the bisectors
'''

from math import pi, sqrt
import matplotlib.pyplot as plt


# Ввод точек
def input_dots():
    x = []
    y = []
    print('\n'*3)
    print('Вводите точки построчно, координаты через запятую!')
    print('\n')
    z = str(input())
    while len(z.split(',')) == 2:
        z = z.split(',')
        x.append(int(z[0]))
        y.append(int(z[1]))
        z = str(input())

    return (x, y)


def find_area(a, b, c):
    p = round((a + b + c) / 2, 5)
    area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 5)
    return area


def find_distance(x1, x2, y1, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Составление всех возможных комбинаций с нахождением разницы площадей
def search(x, y):
    min_difference = 0.0
    x_min = []
    y_min = []
    for ai in range(len(x)):
        for bi in range(ai+1, len(x)):
            for ci in range(bi+1, len(x)):
                ab = find_distance(x[bi], x[ai], y[bi], y[ai])
                ac = find_distance(x[ci], x[ai], y[ci], y[ai])
                #ab/ac = bd/cd
                #intersection between bisector and side (coordinate of the point)
                constant = ab/ac
                xd = (constant*y[ci] + y[bi]) / (1+constant)
                yd = (constant * y[ci] + y[bi]) / (1 + constant)

                bd = find_distance(xd, x[bi], yd, y[bi])
                dc = find_distance(x[ci], xd, y[ci], yd)
                ad = find_distance(xd, x[ai], yd, y[ai])

                area1 = find_area(bd, ad, ab)
                area2 = find_area(dc, ad, ac)
                difference = abs(area1 - area2)
                if min_difference == 0.0:

                    min_difference = difference
                if min_difference > difference and difference > 0.3:
                    min_difference = difference
                    x_min = []
                    y_min = []
                    x_min.append(x[ai])
                    x_min.append(x[bi])
                    x_min.append(x[ci])
                    y_min.append(y[ai])
                    y_min.append(y[bi])
                    y_min.append(y[ci])

    return(x_min, y_min,min_difference)


x_coord, y_coord = input_dots()
x_res, y_res, min_difference_area = search(x_coord, y_coord)
if len(x_res) != 0 :
    print('Искомые точки обладают координатами: ')
    for i in range(len(x_res)):
        print('( {:} ; {:} )'.format(x_res[i], y_res[i]))
    print('Разность площадей треугольников образуваны от бисектриса = {:.4f}'.format(min_difference_area))
    x_res.append(x_res[0])
    y_res.append(y_res[0])
    plt.scatter(x_coord, y_coord)
    plt.plot(x_res, y_res, 'ro-')
    plt.show()
else:
    print('Все точки лежат на 1 прямой!')
