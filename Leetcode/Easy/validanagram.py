s = "anagram"
t = "nagaram"
s_h = {}
t_h = {}

for i in range(len(s)):
    s_h[s[i]] = 1 + s_h.get(s[i], 0)
    t_h[t[i]] = 1 + t_h.get(t[i], 0)
for i in s_h:
    if s_h[i] != t_h.get(i,0):
        print(False)
print(True)
