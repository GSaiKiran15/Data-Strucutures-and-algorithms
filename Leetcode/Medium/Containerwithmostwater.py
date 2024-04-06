height = [2,3,4,5,18,17,6]
area = 0

r = len(height) - 1
l = 0

while l < r:
    max_area = min(height[l], height[r]) * (r-l)
    area = max(area, max_area)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(area) 


#Brute Force
# for i in range(len(height)):
#     for j in range(i, len(height)):
#         curr_area = min(height[i], height[j])*(j-i)
#         if area < curr_area:
#             area = curr_area
# print(area)