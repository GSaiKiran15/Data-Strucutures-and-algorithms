nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

# last = m + n - 1

# while m > 0 and n > 0:
#     if nums1[m-1] > nums2[n-1]:
#         nums1[last] = nums1[m-1]
#         m -= 1
#     else:
#         nums1[last] = nums2[n-1]
#         n -= 1
#     last -= 1

#     while n > 0:
#         nums1[last] = nums2[n-1]
#         n, last = n-1, last-1

nums3 = []

for i in range(m):
    nums3.append(nums1[i])
for i in range(n):
    nums3.append(nums2[i])
for i,j in enumerate(sorted(nums3)):
    nums1[i] = j

print(nums1)

    