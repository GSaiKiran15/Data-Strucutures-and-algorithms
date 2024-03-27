pattern = "abba"
s = "dog dog dog dog"

# Best Solution

if len(s.split()) != len(pattern):
    print(False)

s = s.split()
h1 = {}
h2 = {}

for character, word in zip(pattern, s):
    if character in h1 and h1[character] != word:
        print(False)
    if word in h2 and h2[word] != character:
        print(False)
    h1[character] = word
    h2[word] = character
print(True)


# My Solution

# s = s.split()
# h1 = {}
# h2 = {}
# for i, j in enumerate(pattern):
#     if j in h1 and h1[j] != s[i]:
#         print(False)
#         break
#     else:
#         h1[j] = s[i]
#     if s[i] in h2 and h2[s[i]] != j:
#         print(False, "2nd")  
#     else:
#         h2[s[i]] = j        

# print(h1)
# print(True)
