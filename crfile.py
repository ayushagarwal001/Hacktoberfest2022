file = open('try.txt', 'r')
count = 0
for lines in file:
    if lines!='\n':
        count+=1
file.close()
print(count)
