import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        right = i
        left = right - 1
        while arr[right] < arr[left] and left != -1:
            if arr[right] < arr[left]:
                arr[right], arr[left] = arr[left], arr[right]
                right -= 1
                left = right - 1
    print(arr)

    return arr


arr = random.sample(range(1,1000), 100)
if sorted(insertion_sort(arr)) == arr:
    print(True)
