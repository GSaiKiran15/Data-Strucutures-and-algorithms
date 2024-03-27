prices = [7,6,4,3,1]
if len(prices) < 2:
    print(prices)
else:
    left = 0
    right = 1
    output = prices[right] - prices[left]
    while right < len(prices)-1:
        if prices[right] < prices[left]:
            left = right 
        elif prices[right] > prices[left]:
            if prices[right] - prices[left] > output:
                output = prices[right] - prices[left]
        right += 1
print(0 if output < 0 else output)