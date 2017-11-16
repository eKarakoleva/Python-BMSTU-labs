#Вычисление корней квадратного уравнения
#Караколева Елена  ИУ7-16И
import math as m

op = 'y'
while op == 'y':
    a = input('\nВведите A : ')
    b = input('Введите B: ')
    c = input('Введите C: ')
    #Проверка коректности вывода
    while a == '' or b == '' or c == '':
        print('\n!!!Введите A, B, C (Ax^2+Bx+C)!!!\n')
        a = input('\nВведите A : ')
        b = input('Введите B: ')
        c = input('Введите C: ')
    a=float(a)
    b=float(b)
    c=float(c)
    #Проверка вида уравнения
    if a!=0:
        if b!=0:
            if c!=0:
                dis = b**2 - 4*a*c
                #Проверка дискриминанта
                if dis>0:
                    x1=(-b+m.sqrt(dis))/(2*a)
                    x2=(-b-m.sqrt(dis))/(2*a)
                    print('X1 = %.2f'%x1)
                    print('X2 = %.2f'%x2)
                elif dis<0:
                    print("Нет корней")
                else:
                    x=(-b+m.sqrt(dis))/(2*a)
                    print('X1=X2= %.2f'%x)
            else:
                x1=0;
                x2=-b/a
                print('X1 = %.2f'%x1)
                print('X2 = %.2f'%x2)
        else:
            x=m.sqrt(abs(c/a))
            print('X= ±%.2f'%x)
    else:
        x=-c/b
        print('X=%.2f'%x)
    op=input('\nХотите продольжит? y/n ')
