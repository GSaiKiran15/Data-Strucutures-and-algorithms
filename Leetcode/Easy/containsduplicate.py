nums = [1,0,1,1]
k = 1
h = {}

for i in range(len(nums)):
    if nums[i] in h:
        print(h[nums[i]])
        if abs(h[nums[i]] - i) <= k:
            print(True)
        elif abs(h[nums[i]] - i) >= k:
            h[nums[i]] = i
    else:
        h[nums[i]] = i
print(False) 