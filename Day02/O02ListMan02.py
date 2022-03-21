
"""
'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort'
"""

# functions which can add elements into the list - append, extend, insert

print("append".center(40, "-"))
l1 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.9, 9.5, True, False, 8+9j, 11 + 25j]
print(f"l1 :{l1}")

l1.append(20)
l1.append("apple")
print(f"l1 :{l1}")

l1.append([21, 22, 23, 24, 25])
print(f"l1 :{l1}")
print(f"l1[15] :{l1[15]}")
print(f"l1[15] :{l1[15][1:4]}")

print("extend".center(40, "-"))
l2 = list(range(1, 6))
print(f"l2 :{l2}")
l2.extend([6, 7, 8, 9, 10])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l = list(range(1, 6))
print(f"l :{l}")
l.insert(1, 1.5)
l.insert(3, 2.5)
l.insert(5, 3.5)
print(f"l :{l}")

# remove elements from the list - pop, remove
print("remove".center(40 ,"-"))
l1 = [1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1,1,1,1,1,1]
print(f"l1 :{l1}")
res = l1.remove(1)
print(f"res :{res}")
print(f"l1 :{l1}")

while True:
    try:
        l1.remove(1)
    except ValueError:
    # except Exception as e:
        # print(e)
        break

print(f"l1 :{l1}")

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

# l1.pop(9)
