print("started")


def get_count(strb):    
    ln = [len(strb)]
    print(ln)
    return ln

def get_data(strng):
    l3=[]
    l3 = strng.split(",")
    print(l3)
    lst = []
    print(l3[0])
    lst = get_count(l3[1])
    print(lst)
    return lst

lst  = get_data("hello my friend, ho are you")
print(lst)

print("ended")
