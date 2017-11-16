import math as m

x = float(input('Enter X: '))
eps = float(input('Enter epsilon: '))
n_iter = float(input('Enter number of iterations: '))
n = float(input('Enter step/шаг: '))
d=3
sum_x = 0
k = x
n_op = 0
sos = 0
t=x

print(' _______________________________________')
print('│  Шаг  │    Тек.член   │     Сумма     │')
while t >= eps:
    sum_x +=t
    step = n_op%n
    if n_op >= n_iter:
        print(' _______________________________________')
        print()
        print('Ряд не сошолься')
        sos = 1;
        break;
    if step == 0:
        print('│ %5.d │ %13.4f │ %13.4f │' % (n_op,t,sum_x))
        
    k = k * (x**2)
    t = k/d

    d+=2;
    n_op += 1

if sos !=1:
    print(' _______________________________________')
    print()
    print("Сумма = %.3f"%sum_x)




