import math as m

a = float(input("Enter 'a' in [a,b]: "))
b = float(input("Enter 'b' in [a,b]: "))
n = int(input("Enter num of parts: "))

res_1=[]
res_2=[]
count = 0
parts_arr = []
parts_arr.append(n)
while count != 2:
    step = (b-a)/n
    x0 = a
    arr_xs_sim = [x0]
    arr_xs_prqm = [x0]

    for i in range(n):
        x0+=step
        arr_xs_sim.append(round(x0,3))
        arr_xs_prqm.append(round(x0,3))
        
    #2 
    arr_xs_prqm_steps = [] 
    for i in range(len(arr_xs_prqm)-1):
        f_x = arr_xs_prqm[i]+(step/2)
        arr_xs_prqm_steps.append(round(f_x,3))
    #1   
    arr_fun_sim = []  
    for i in range(len(arr_xs_sim)):
        arr_fun_sim.append(round(1/m.log(arr_xs_sim[i]),3))

    #1
    fun0_sim = (arr_fun_sim[0] - arr_fun_sim[len(arr_xs_sim)-1])/2
    integ_sim = fun0_sim
    for i in range(1,len(arr_fun_sim)):
        integ_sim+=arr_fun_sim[i]
    res_1.append(abs(round(integ_sim*step,3))) #fisrt

    #2   
    integ_prqm = 0
    for i in range(len(arr_xs_prqm_steps)):
        fun_fun_prqm = round(1/m.log(arr_xs_prqm_steps[i]),3)
        integ_prqm += fun_fun_prqm
        
    res_2.append(abs(round(integ_prqm*step,3)))   
    count +=1
    if count!=2:
        n = int(input("Enter num of parts: "))
        parts_arr.append(n)
        
print()

print('│ Части │ Симсона │ Средних прям │')

for i in range(len(res_1)):
    print('│   %1.d   │ %7.4f │   %7.4f    │' % (parts_arr[i],res_2[i],res_2[i]))

