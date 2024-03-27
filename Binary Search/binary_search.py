def binary_search(arr, target):
    
    start, end = 0, len(arr)-1

    while start <= end:
        
        mid = (start + end) // 2
        
        if arr[mid] == target:
            print(f"Found at index {mid}")
            return
        
        elif arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid 

    print("Not Found")
    return

arr = [1, 9, 20, 36, 45, 81]
binary_search(arr, 82)