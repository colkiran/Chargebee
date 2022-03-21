

print("count".center(40, "-"))
l = [1, 2, 1, 2, 1, 3, 2, 1, 1, 2, 3, 4, 1]
print(f"l.count(1) :{l.count(1)}")
print(f"l.count(2) :{l.count(2)}")
print(f"l.count(5) :{l.count(5)}")

print("index".center(40, "-"))
l = [1, 2, 1, 2, 3, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3]
print(f"l :{l}")
print(f"l.index(1) :{l.index(1)}")
print(f"l.index(3) :{l.index(3)}")
print(f"l.index(3) :{l.index(3, 5, 10)}")
print(f"l.index(3) :{l.index(3, 9)}")
# print(f"l.index(4) :{l.index(4)}")

print('copy'.center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1             # shallow copy -> not only shares the data but also shares the address
print(f"l2 Before :{l2}")

print("-" * 40)
l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
# copy()
l3 = [6, 7, 8, 9, 10]
print(f"l3 Before :{l3}")
l4 = l3.copy()          # Deep copy -> only the values are copied
print(f"l4 Before :{l4}")

print("-" * 40)
l4.insert(1, 6.5)
l4.insert(3, 7.5)
l4.insert(5, 8.5)
l4.insert(7, 9.5)
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

print("-" * 40)
l6[4].insert(1, 11.5)
l6[4].insert(3, 22.5)
l6[4].insert(5, 33.5)
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

from copy import deepcopy
l7 = [1, 2, [10, 20, 30, 40, 50], 3, 4, 5]
print(f"l7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

print("-" * 40)
l8[2].insert(1, 15)
l8[2].insert(3, 25)
l8[2].insert(5, 35)
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")

