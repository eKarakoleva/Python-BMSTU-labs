'''
Reorder array:
Put odd numbers on the left
and even numbers on the right without changing
the order.
'''

arr = list(map(int,input('Enter numbers:').split()))
temp=0
if len(arr) <= 90:
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]%2==0 and arr[j+1]%2!=0:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)
else:
    print("Array must be less than 90 numbers!")


        

