
mercedes = ["E350", "C200", "C180"]

print(mercedes[0])
print(mercedes[-1])
print(mercedes[1:])

mercedes.append("W211")

mercedes.insert(3,"W203")

print(mercedes)

print(mercedes.index("C200"))

mercedes.sort()
print(mercedes)

mercedes.reverse()
print(mercedes)

mercedes2 = mercedes.copy()
print(mercedes)