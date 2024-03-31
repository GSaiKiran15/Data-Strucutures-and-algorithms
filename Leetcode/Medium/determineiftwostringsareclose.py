from collections import Counter

word1 = "abc"
word2 = "bca"

c1 = Counter(word1)
c2 = Counter(word2)

n1 = Counter([n for n in c1.values()])
n2 = Counter([n for n in c2.values()])

print(c1 == c2 or (n1 == n2 and set(word1) == set(word2)))

# h1 = {}
# h2 = {}
# if len(word1) != len(word2):
#     print(False)
# else:
#     for i in word1:
#         if i not in word2:
#             print(False)
#             break
#         if i in h1:
#             h1[i] += 1
#         else:
#             h1[i] = 1
#     for i in word2:
#         if i in h2:
#             h2[i] += 1
#         else:
#             h2[i] = 1
# arr1 = []
# arr2 = []
# for i in h1.values():
#     arr1.append(i)
# for i in h2.values():
#     arr2.append(i)
# if sorted(arr1) == sorted(arr2):
#     print(True)
# else:
#     print(False)