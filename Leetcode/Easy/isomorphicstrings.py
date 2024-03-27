s = "egg"
t = "add"
s_map = {}
t_map = {}
for i, j in zip(s,t):
    if i in s_map:
        s_map[i] += 1
    else:
        s_map[i] = 1
    if j in t_map:
        t_map[j] += 1
    else:
        t_map[j] = 1
count = 0
for u in s_map:
    print(s_map[u])