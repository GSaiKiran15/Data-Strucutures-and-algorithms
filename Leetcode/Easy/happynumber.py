n = 19
n = str(n)
h = {}
while sum != 1:
    sum = 0    
    for i in n:
        sum += int(i)**2
    if sum in h:
        print(False)
        break
    elif sum == 1:
        print(True)
        break
    h[sum] = 0
    n = str(sum)
print(h)
