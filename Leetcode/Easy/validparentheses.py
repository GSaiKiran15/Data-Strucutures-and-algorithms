s = "()[]{"

h = {
    "]":"[",
    "}":"{",
    ")":"("
}

stack = []

for i in s:
    if i in h:
        if stack and h[i] == stack[-1]:
            stack.pop()
        else:
            print(False)
    else:
        stack.append(i)

print(True) if not stack else print(False)

# hash_map = {
#     "}" : "{",
#     "]" : "[", 
#     ")" : "(",   
# }

# stack = []

# for i in s:
#     if i in hash_map:
#         if stack and hash_map[i] == stack[-1]:
#             stack.pop()
#         else:
#             print(False)
#     else:
#         stack.append(i)

# print(True) if not stack else print("False")

    