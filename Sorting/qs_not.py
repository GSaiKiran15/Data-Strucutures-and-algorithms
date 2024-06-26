def swap(a, b, arr):
    arr[a] , arr[b] = arr[b], arr[a]

def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1
    
    while start < end:

        while elements[start] <= pivot:
            start += 1
        
        while elements[end] >= pivot:
            end -= 1
        
        if start < end:
            swap(pivot_index, end, elements)
        
    print(elements)

partition([11, 9, 29, 7, 2, 15, 28])

