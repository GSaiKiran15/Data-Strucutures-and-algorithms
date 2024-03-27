haystack = "leetcode"
needle = "leeto"
right = len(needle)-1
left = 0

if len(haystack) >= len(needle):
    while right <= len(haystack)-1:
        count = 0
        for i, j in enumerate(range(left, right+1)):
            if needle[i] != haystack[j]:
                right += 1
                left += 1
                break
            else:
                count += 1
        if count == len(needle):
            print(left)
            break
    print(-1)
else:
    print(-1)

