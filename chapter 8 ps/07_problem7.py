def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Kanna", "Sid", "John", "id"]

print(rem(l,"id"))