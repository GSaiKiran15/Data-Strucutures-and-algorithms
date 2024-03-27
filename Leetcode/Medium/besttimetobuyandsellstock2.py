prices = [7,1,5,3,6,4]
# l, r = 0, 1
output = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        output += prices[i] - prices[i-1]
print(output)
# while r <= len(prices)-1:
#     if prices[l] > prices[r]:
#         l += 1
#         r += 1
#     else:
#         output += prices[r] - prices[l]
#         r += 1
#         l += 1
# print(output)

    # if prices[l] > prices[r]:
    #     l += 1
    #     r += 1
    # if r<= len(prices)-1 and prices[l] < prices[r]:
    #     p = r
    #     r += 1
    #     while r<= len(prices)-1 and prices[p] < prices[r]:
    #         p = r
    #         r += 1
    #     output += prices[p] - prices[l]
    #     l = r
    #     r += 1