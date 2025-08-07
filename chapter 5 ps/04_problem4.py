s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))

# length of s would be 2 as the vlaues 20 ==20.0 --> True in python