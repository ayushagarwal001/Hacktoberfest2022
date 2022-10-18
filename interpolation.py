a = [1, 5 , 13 ,12 ,16,19,21,24,29,31,46,89,90,104]
x = 10
low = 0
high = len(a)-1
while low<=high:
    pos = low + (x-a[low])*(high-low) / (a[high]-a[low])
    pos = round(pos)
    if a[pos] == x:
        print("found",pos)
        break
    elif x<a[pos]:
        high = pos - 1
    elif x>a[pos]:
        low = pos + 2
if low > high:
    print("not found")