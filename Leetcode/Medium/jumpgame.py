nums = [3,2,1,0,4]
i = 0
while i <= len(nums):
    if i == len(nums)-1:
        print(True)
        break
    if nums[i] <= 0 and i != len(nums)-1:
        print(False)
        break
    i += nums[i]
print(False)
