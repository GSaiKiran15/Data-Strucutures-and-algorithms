import random

arr = random.sample(range(1,1000), 100)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    return arr

selection_sort(arr)
    
