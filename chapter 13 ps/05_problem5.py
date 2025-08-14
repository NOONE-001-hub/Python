from functools import reduce
l = [111,35, 4,43, 441, 23, 35,53]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))


