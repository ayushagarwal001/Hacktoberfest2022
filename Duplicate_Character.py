print("Enter the String: ", end="")
str = input()

strlist = list()
for i in range(len(str)):
    strlist.append(str[i])

newlist = list()
j = 0
for i in range(len(strlist)):
    if str[i] not in newlist:
        newlist.insert(j, str[i])
        j = j+1

print("\nOriginal String =", str)

newstr = ""
for c in newlist:
    newstr = newstr + c
print("New String =", newstr)
