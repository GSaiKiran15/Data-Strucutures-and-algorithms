nums = [0,2,3,4,6,8,9]
output = []
ranger = f""
pre = 0
l = 0
r = 1

while r <= len(nums)-1:
    if l == len(nums)-1:
        output.append(f"{nums[l]}")
    if (nums[l]+1) == nums[r]:
        l += 1
        r += 1
    else:
        output.append(f"{nums[pre]}->{nums[r-1]}")
        l = r
        pre = r
        r += 1
print(output)
# for i in range(len(nums)-1):
#     if (nums[i] + 1) == nums[i+1]:
#         next_number = nums[i+1] 
#     elif (nums[i] + 1) != nums[i+1]:
#         if prev_number == next_number:
#             ranger = f"{prev_number}"
#         else:
#             ranger += f"{prev_number}->{next_number}"
#         output.append(ranger)
#         ranger = ""
#         prev_number = nums[i+1]
#         next_number = nums[i+1]
# print(output)