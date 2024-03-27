s = "abc"
t = "ahbgdc"
index = 0
for i in t:
    if i == s[index]:
        index += 1
        if index == len(s):
            print(True)
print(False)


