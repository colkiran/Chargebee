
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': '1', 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f'd2 :{d2}')
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 87), ('opp', 'NZL'), ('venue', 'Auckland'), ('year', 1998)])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='sachin', runs=87, opp='NZL', venue='Auckland', year=1998)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
d5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d5 :{d5}")
print(type(d5))

print(f"d5['c'] :{d5['c']}")
print(f"d5['a'] :{d5['a']}")

d5['b'] = 200           # update the value of the key
d5['f'] = 60            # add a new key value pair
del d5['a']             # delete the key and value

print(f"d5 :{d5}")
d5['z'] = None          # None is null in python
print(f"d5 :{d5}")

d5['a'] = 1
print(f"d5 :{d5}")

print('a' in d5)
print('c' not in d5)

print("-" * 40)
for i in d5:
    print(i, end=" ")
print()

print("-" * 40)
print(d5.get('j', "Invalid Key, Please enter a valid key"))
print(d5.get('b'))

print("-" * 40)
print(dir(d5))
