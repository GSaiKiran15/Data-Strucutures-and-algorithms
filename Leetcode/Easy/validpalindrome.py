s = "A man, a plan, a canal: Panama"
output = ""
for i in s:
    if i.isalnum():
        output += str(i).lower()
if output == output[::-1]:
    print(True)
    # return True
else:
    print(False)
