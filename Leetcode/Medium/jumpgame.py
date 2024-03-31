nums = [2,3,1,1,4]

#Best Solution

goal = len(nums)-1

for i in range(len(nums)-1, -1, -1):
    print(i)
    if i + nums[i] >= goal:
        goal = i
print(True if goal == 0 else False)

# My solution
# if len(nums) > 1:
#     i = -2
#     goal = -1
#     while i > -len(nums):
#         if i + nums[i] >= goal:
#             goal = i
#         i -= 1
#     if goal == -len(nums):
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)