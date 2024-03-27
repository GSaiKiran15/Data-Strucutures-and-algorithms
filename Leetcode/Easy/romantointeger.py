roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

s = "MCMXCIV"
output = 0
left = 0
right = 1
while right <= len(s)-1:
    print(s[left], s[right], output)
    if roman[s[left]] < roman[s[right]]:
        output += (roman[s[right]]-roman[s[left]])
        left = right + 1
        right += 2
    else:
        output += roman[s[left]]
        right += 1
        left += 1
if left <= len(s)-1:
    output += roman[s[-1]]
print(output)
