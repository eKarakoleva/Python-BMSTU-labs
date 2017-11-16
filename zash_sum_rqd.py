import math as m

x = float(input('Enter X: '))
eps = float(input('Eps:'))
n_iter = float(input('Enter number of iterations: '))
s_sum = 1
t = 1
d=1
n_op = 0
sos = 0
while abs(t) >= eps:
    print('│ %5.d │ %13.4f │ %13.4f │' % (n_op,t,s_sum))
    if n_op >= n_iter:
        print('Ряд не сошолься')
        sos = 1
        break;
    if t == 1:
        t = 2*x
        s_sum += t
        n_op +=1
    else:
        t = (t * x)/(round(m.factorial(d)))
        s_sum += t
        d = d+1
        n_op+= 1
if sos == 0:
    print(s_sum)
 

