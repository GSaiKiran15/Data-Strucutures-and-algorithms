nums = [2,7,11,15]
target = 9

# Better Solution

# hash_map = {}

# for i in range(len(nums)):
#     if target - nums[i] in hash_map:
#         print([i,hash_map[target - nums[i]]])
#     else:
#         hash_map[nums[i]] = i

 
#my solution

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i,j])
#             break
