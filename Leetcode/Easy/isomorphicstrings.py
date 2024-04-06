s = "badc"
t = "baba"
s_map = {}
t_map = {}

for c1, c2 in zip(s, t):
    if ((c1 in s_map and s_map[c1] != c2) or (c2 in t_map and t_map[c2] != c1)):
        print(False)
    s_map[c1] = c2
    t_map[c2] = c1
print(True)

for i in range(len(s)):
    if s[i] not in s_map:
        s_map[s[i]] = t[i]
    if t[i] not in t_map:
        t_map[t[i]] = s[i]
    if t[i] != s_map[s[i]] or s[i] != t_map[t[i]]:
            print(False)
print(True)