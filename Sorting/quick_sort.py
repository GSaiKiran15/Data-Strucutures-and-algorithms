def quick_sort(elements):
    pivot = 0
    start = pivot + 1 
    end = len(elements)-1
    while start < end:
        for _ in range(len(elements)-1):
            if elements[start] > elements[pivot]:
                break
            else:
                start += 1
        for _ in range(len(elements)-1):
            if elements[end] < elements[pivot]:
                elements[start], elements[end] = elements[end], elements[start]
                break
            else:
                if end != 0:
                    end -= 1
        if end < start:
            elements[pivot], elements[end] = elements[end], elements[pivot]

        pivot += 1
        

elements = [11, 9, 29, 7, 2, 15, 28]
quick_sort(elements)
print(elements)