import math as m

#Вычисление углов
def angle (a, b, c):
    return round(m.degrees(m.acos((c**2 - b**2 - a**2)/(-2.0 * a * b))))

#Вычисление длины медианы
def mediana(a, b, c):
    return 1/2*(m.sqrt(2*a**2+2*b**2-c**2))

#Вычисление площади треугольника
def area(x1,y1,x2,y2,x3,y3):
   return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2)

def isInside(x1,y1,x2,y2,x3,y3,xp,yp):
   #Calculate area of triangle ABC 
   A = area(x1, y1, x2, y2, x3, y3)
   #Calculate area of triangle PBC
   A1 = area(xp, yp, x2, y2, x3, y3)
   #Calculate area of triangle PAC
   A2 = area(x1, y1, xp, yp, x3, y3)
   #Calculate area of triangle PAB  
   A3 = area(x1, y1, x2, y2, xp, yp)
   #Check if sum of A1, A2 and A3 is same as A
   return (A == A1 + A2 + A3)

def disToSide(dlin_ab,dlin_ca,dlin_bc):
     A1 = area(xp, yp, x2, y2, x3, y3)
     h1 = (2*A1)/dlin_ab;
     A2 = area(x1, y1, xp, yp, x3, y3)
     h2 = (2*A2)/dlin_ca;
     A3 = area(x1, y1, x2, y2, xp, yp)
     h3 = (2*A3)/dlin_bc;
     Max = max(h1,h2,h3)
     return Max   
     


x1,y1=map(int,input('Ведите координаты точки А(x1;y1):').split(';'))
x2,y2=map(int,input('Ведите координаты точки B (x2;y2):').split(';'))
x3,y3=map(int,input('Ведите координаты точки C (x3;y3):').split(';'))

koord_ab_x = x2-x1
koord_ab_y = y2-y1
koord_ca_x = x1-x3
koord_ca_y = y1-y3
koord_bc_x = x2-x3
koord_bc_y = y2-y3

dlin_ab = m.sqrt(koord_ab_x**2 + koord_ab_y**2)
dlin_ca = m.sqrt(koord_ca_x**2 + koord_ca_y**2)
dlin_bc = m.sqrt(koord_bc_x**2 + koord_bc_y**2)

print('\nКоординати AB(%.d;%.d)'%(koord_ab_x,koord_ab_y))
print('Координати CA(%.d;%.d)'%(koord_ca_x,koord_ca_y))
print('Координати BC(%.d;%.d)\n'%(koord_bc_x,koord_bc_y))

print('Длина AB = %.3f'%dlin_ab)
print('Длина CA = %.3f'%dlin_ca)
print('Длина BC = %.3f\n'%dlin_bc)

if area(x1, y1, x2, y2, x3, y3) != 0:
    angA = angle(dlin_bc,dlin_ca,dlin_ab)
    angB = angle(dlin_ca,dlin_ab,dlin_bc)
    angC = angle(dlin_ab,dlin_bc,dlin_ca)

    print('Угол A = %.3f'%angA)
    print('Угол B = %.3f'%angB)
    print('Угол C = %.3f\n'%angC)

    Min = angA
    ang='A'
    med = mediana(dlin_ab,dlin_ca,dlin_bc)
    if angB < Min:
        Min = angB
        med = mediana(dlin_ab,dlin_bc,dlin_ca)
        ang = 'B'
    if angC < Min:
        Min = angC
        med = mediana(dlin_bc,dlin_ca,dlin_ab)
        ang='C'
    if angB < angC:
        Min = angB
        med = mediana(dlin_ab,dlin_bc,dlin_ca)
        ang = 'B'

    print('Наименший угол %s = %.3f'%(ang,Min))
    print('Медиана от наименшего угла = %.3f\n'%med)


    xp,yp=map(int,input('Введите координати точки P (x4;y4):').split(';'))

    isIn = isInside(x1,y1,x2,y2,x3,y3,xp,yp)

    if isIn == True:
        print('Точка находится внутри треугольника')
        print('Длина от точки до наиболее удаленной стороны = %f'%disToSide(dlin_ab,dlin_ca,dlin_bc))
    else:
        print('Точка НЕ находится в треугольника')

    if (dlin_ab == dlin_bc == dlin_ca) or (dlin_ab != dlin_bc != dlin_ca):
        print("Треуголньник НЕ равнобедренный")
    else:
        print("Треуголньник - равнобедренный")
else:
    print("Точки на одной прямой")

