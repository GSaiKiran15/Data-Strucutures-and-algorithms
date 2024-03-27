nums = [0,1,2,2,3,0,4,2]
val = 2

# for i in nums[:]:
#     if i == val:
#         nums.remove(i)

while val in nums:
    nums.remove(val)

# k = 0
# while k < len(nums):
#     if nums[k] == val:
#         nums.remove(val)
#     else:
#         k += 1

print(len(nums))