def divisibles(n):
    if(n%5 == 0):
        return True
    return False

a = [1,3, 4,43455, 44, 23425, 35355,53345345]

f = list(filter(divisibles, a))
print(f)