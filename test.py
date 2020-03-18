import math
dictionary = {'23':16, '20':25}
finall2 = 0
for values in dictionary.values():
    finall = math.sqrt(values)
    finall2 += finall
print(finall2)

