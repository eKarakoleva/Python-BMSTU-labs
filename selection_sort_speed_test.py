import timeit
import numpy as np
from tkinter import *
from tkinter import ttk


#  selection sort (sorting any array)
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        nmin = i
        for j in range(i + 1, n):
            if array[j] < array[nmin]:
                nmin = j
        array[i], array[nmin] = array[nmin], array[i]
    return array


#  generate random array of "n" size and put result in entry
#  sort array and put sorted array in another entry
def sort_array():
    size = size_array.get()
    if size > 0 and size <= 10:
        x = np.random.randint(100, size=size)
        unsorted_array.set("")
        sorted_array.set("")
        unsorted_array.set(x)
        sorted_array.set(selection_sort(x))
    else:
        unsorted_array.set("")
        sorted_array.set("")
        unsorted_array.set("Enter number in the interval [1;10]")


# when button is pressed function generate arrays of 100, 1000 and 10000 elements
# sort arrays and measure sorting time
#put result in ttk table
def run_test():

    # generate arrays
    array_100_desc = [x for x in range(100, 0, -1)]
    array_1000_desc = [x for x in range(1001, 0, -1)]
    array_10000_desc = [x for x in range(10001, 0, -1)]

    array_100_asc = [x for x in range(1, 101, 1)]
    array_1000_asc = [x for x in range(1, 1001, 1)]
    array_10000_asc = [x for x in range(1, 10001, 1)]

    array_100_rand = list(np.random.randint(1000, size=100))
    array_1000_rand = list(np.random.randint(10000, size=1000))
    array_10000_rand = list(np.random.randint(100000, size=10000))

    #arrays for the time results of every kind
    time_array_rand = []
    time_array_asc = []
    time_array_desc = []

    # sorting and measuring asc
    print("array_100_asc")
    start = timeit.default_timer()
    selection_sort(array_100_asc)
    end = timeit.default_timer() - start
    time_array_asc.append(end)

    print("array_1000_asc")
    start = timeit.default_timer()
    selection_sort(array_1000_asc)
    end = timeit.default_timer() - start
    time_array_asc.append(end)

    print("array_10000_asc")
    start = timeit.default_timer()
    selection_sort(array_10000_asc)
    end = timeit.default_timer() - start
    time_array_asc.append(end)

    # sorting and measuring desc
    print("array_100_desc")
    start = timeit.default_timer()
    selection_sort(array_100_desc)
    end = timeit.default_timer() - start
    time_array_desc.append(end)

    print("array_1000_desc")
    start = timeit.default_timer()
    selection_sort(array_1000_desc)
    end = timeit.default_timer() - start
    time_array_desc.append(end)

    print("array_10000_desc")
    start = timeit.default_timer()
    selection_sort(array_10000_desc)
    end = timeit.default_timer() - start
    time_array_desc.append(end)

    # sorting and measuring random
    print("array_100_rand")
    start = timeit.default_timer()
    selection_sort(array_100_rand)
    end = timeit.default_timer() - start
    time_array_rand.append(end)

    print("array_1000_rand")
    start = timeit.default_timer()
    selection_sort(array_1000_rand)
    end = timeit.default_timer() - start
    time_array_rand.append(end)

    print("array_10000_rand")
    start = timeit.default_timer()
    selection_sort(array_10000_rand)
    end = timeit.default_timer() - start
    time_array_rand.append(end)

    # create ttk treeview (for creating the table)
    tree = ttk.Treeview(root)
    tree["columns"] = ("one", "two", "three")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.heading("one", text="100")
    tree.heading("two", text="1 000")
    tree.heading("three", text="10 000")

    # element 0 - 100 elements time_array_[0]
    # element 1 - 1 000 elements time_array_[1]
    # element 2 - 10 000 elements time_array_[2]

    tree.insert("", 0, text="Random", values=(time_array_rand[0], time_array_rand[1], time_array_rand[2]))
    tree.insert("", 0, text="Ascending", values=(time_array_asc[0], time_array_asc[1], time_array_asc[2]))
    tree.insert("", 0, text="Descending", values=(time_array_desc[0], time_array_desc[1], time_array_desc[2]))

    tree.pack()


# create frame with 3 entries and 1 button
root = Tk()
frame = Frame(root, width=50, height=15, bd=1)
frame.pack()
iframe1 = Frame(root, bd=2, relief=SUNKEN)
# create button that calls sort_array() fuction
Button(iframe1, text='Sort', command=sort_array).pack(side=LEFT, padx=5)
Label(iframe1, text="Enter size: ").pack(side=LEFT, padx=5)

size_array = IntVar()
e = Entry(iframe1, textvariable=size_array ,width=5).pack(side=LEFT, padx=5)

Label(iframe1, text="Array:").pack(side=LEFT, padx=5)
unsorted_array = IntVar()
e1 = Entry(iframe1, textvariable=unsorted_array,width=25).pack(side=LEFT)
Label(iframe1, text="Sorted array:" ).pack(side=LEFT, padx=5)
sorted_array = IntVar()
e2 = Entry(iframe1, textvariable=sorted_array,width=25).pack(side=LEFT)
iframe1.pack(expand=1, fill=X, pady=10, padx=5)

# create button that calls run_test() fuction
Button(root, text='Run test', command=run_test).pack(side=LEFT, padx=5)

root.mainloop()