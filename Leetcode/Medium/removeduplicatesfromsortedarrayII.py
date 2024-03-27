nums = [0,0,1,1,1,1,2,3,3]
h = {}
p = 0
while p <= len(nums)-1: 
    if not h.get(nums[p]):
        h[nums[p]] = 1
        p += 1
    else:
        if h[nums[p]] >= 2:
            nums.remove(nums[p])
        else:
            h[nums[p]] += 1
            p += 1
print(len(nums), nums) 