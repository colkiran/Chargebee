
"""
lists are mutable
list are ordered collection

"""

l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 5]
print(f"12: {l2}")

print("-" * 40)
l3 = list(range(1, 11))
print(f'l3 :{l3}')

print("-" * 40)
l4 = list(range(1, 6))
print(f"l4 :{l4}")
print(f"l4[0] :{l4[0]}")
print(f"l4[-1] :{l4[-1]}")
print(f"l4[0:] :{l4[0:3]}")
print(f"l4[:] :{l4[:]}")

print(f"l4[-:-5:-1] :{l4[-1:-5:-1]}" )
print(f"l4[::-1] :{l4[::-1]}")

print("-" * 40)
print(f"l4 :{l4}")
l4[2] = 33
print(f"l4 :{l4}")
# l4[5] = 55

print("-" * 40)
print(dir(l4))
