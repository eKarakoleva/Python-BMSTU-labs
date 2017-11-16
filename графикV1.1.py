#Караколева Елена ИУ7-16И

from math import pi, cos, sqrt, tan, exp

x = float(input('Введите начальное значение Х): '))
x0 = x
t = float(input('Введите шаг: '))
k = float(input('Введите конечное значение Х: '))

i = 0
y = []
#построение таблицы
print(' ________________________________________________')
print('│      x         │      y1       │      y2       │')
print()
while x < k:
    y.append(exp(-x) + (x-1)**2 -3) #первая функция
    h = pow(x,4)-3*pow(x,3)+8*pow(x,2)-5 #вторая функция

    print('│','%13.3f' % (x), end = '  │') 
    print('%13.3f' % (y[i]), end = '  │')
    print('%13.3f' % (h), end = '  │')
    
    print()
    i+=1
    x += t
print(' ________________________________________________')
    
print()
print()

f_max = max(y)
f_min = min(y)
z = round((0 - f_min)/(f_max - f_min) * 60) #находим позицию нуля.
print(' '*(z+8) + 'x')
s = ''    
j=0
a = 0
d0 = round((y[0] - f_min)/(f_max - f_min) * 60)
#находим позицию каждого элемента и печатаем график.
while x0 < k: 
    d = round((y[j] - f_min)/(f_max - f_min) * 60)
    if(x0>0):
        print(" ", end='')
    #отрицательные значения Х
    if d < z:
        if (abs(x0)) < 0.1 and abs(x0) > -0.1 and a!=1:
            a=1
            s = '─' * (d) + '*' + '─'*d0+' y'
            print(' %5.3f' % (abs(x0)), s)
        else:
            s = ' ' * (d) + '*' + ' ' * (z - d) + '│'
            print('%5.3f' % (x0), s)
                  
    #значение совпадает с осью Х
    elif d == z:
        s = ' ' * (d) + '*'
        print('%5.3f' % (x0), s)

    #положительные значения Х 
    else:
        s = s = ' ' * (z + 1) + '│' + ' ' * (d - z) + '*'
        print('%5.3f' % (x0), s)
           
    x0 += t
    j+=1

