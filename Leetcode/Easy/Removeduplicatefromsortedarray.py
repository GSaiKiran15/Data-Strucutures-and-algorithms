nums = [0,0,1,1,1,2,2,3,3,4]
# right = 1
# left = 0
# if len(nums) >= 2:
#     while right <= len(nums)-1:
#         if nums[left] == nums[right]:
#             nums.remove(nums[right])
#         else:
#             left += 1
#             right += 1


l = 1

for r in range(1,len(nums)):
    if nums[r] != nums[r-1]:
        nums[l] = nums[r]
        l += 1
print(l)
print(nums)