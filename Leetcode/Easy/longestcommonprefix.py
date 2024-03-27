strs = ["flower","flow","flight"]
min_length = min(len(s) for s in strs)
iterator = 0
output = ""
while iterator <= min_length-1:
    for i in strs:
        if i[iterator] != strs[0][iterator]:
            break
    output += i[iterator]
    iterator += 1
print(output)
