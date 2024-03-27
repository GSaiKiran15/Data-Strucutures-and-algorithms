nums = [-1,0,3,5,9,12]
target = 2
left = 0
right = len(nums)-1
while left < right:
    mid = (right + left) // 2
    if target == nums[mid]:
        print(f"Target Found {mid}")
        break
    elif nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
print("Not Found")
     