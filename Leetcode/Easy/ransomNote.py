ransomNote = "aabbcc"
magazine = "aaccbb"

# Best solution

m = {}
for i in magazine:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1

for i in ransomNote:
    if i not in m or m[i] == 0:
        print(False)
        break
    else:
        m[i] -= 1
print(True)


# My solution 

# r = {}
# m = {}
# for i in ransomNote:
#     if i in r:
#         r[i] += 1
#     else:
#         r[i] = 1

# for i in magazine:
#     if i in m:
#         m[i] += 1
#     else:
#         m[i] = 1
# count = 0
# for i in r:
#     print(r[i], m[i])
#     if r[i] == m[i]:
#         count += 1

# print(True if count == len(r) else False)