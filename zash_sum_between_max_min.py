import math as m

arr = list(map(int, input('Enter array: ').split()))

sum_el = 0
i=0
max_elem_index = arr.index(max(arr))
min_elem_index = arr.index(min(arr))
if max_elem_index < min_elem_index:
    for el in arr:
        if arr.index(el) > max_elem_index and arr.index(el) < min_elem_index:
            sum_el += el
            i+=1
else:
    for el in arr:
        if arr.index(el) > min_elem_index and arr.index(el) < max_elem_index:
            sum_el += el
            i+=1
print(sum_el/i)
