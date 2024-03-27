import random

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for inner_loop in range(len(arr)-(i+1)): # This slicing helps in reducing the time complexity by reducing the number of elements checked with each iteration.
            if arr[inner_loop] > arr[inner_loop + 1]:
                arr[inner_loop], arr[inner_loop + 1] = arr[inner_loop + 1], arr[inner_loop]
    return arr

arr = random.sample(range(1,1000), 100)

if sorted(bubble_sort(arr)) == arr:
    print(True)