numbers = [0,0,3,4]
target = 0

# Best Solution

left = 0
right = len(numbers)-1
while left < right:
    value = numbers[left] + numbers[right]
    if value < target:
        left += 1
    elif value > target:
        right -= 1
    else:
        print(left+1, right+1)
        break

# My Solution

# h = {}
# for i in range(len(numbers)):
#     if i not in h:
#         h[numbers[i]] = i
#     if (target - numbers[i]) in h and h[(target - numbers[i])] != i:
#         print(h[(target - numbers[i])]+1, i+1)
# print([])