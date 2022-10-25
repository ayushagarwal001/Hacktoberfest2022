array = [0, 1]
pisano = []
n = int(input("Enter Number: "))
for i in range(1, n-1):
    array.append(array[i-1] + array[i])
print (array)


for i in range(2, 7):
    for j in range(0,len(array)):
        mod = array[j] % i
        pisano.append(mod)
    print("Fibo Element mod " + str(i) + ": ", end="")
    print(pisano)
    pisano = []
