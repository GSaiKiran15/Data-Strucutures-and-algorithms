nums = [2,2,1,1,1,2,2,1,1,1,1]

# hash_map = {}
# for i in nums:
#     if i not in hash_map:
#         hash_map[i] = 1
#     else:
#         hash_map[i] += 1
# print(max(hash_map.items(), key=lambda item: item[1])[0])

count = 1
result = nums[0]

for i in range(1, len(nums)):
    if nums[i] == result:
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            count = 1
            result = nums[i]
print(result)