
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

print("keys".center(40, "-"))
player = {'name': 'Rahul', 'runs': 125, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2001}
print(f"player :{player}")
print(player['name'])

# keys
k = player.keys()
print(f"k :{k}")
for i in k:
    print(i, end=" ")
print()

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Rahul', 'runs': 125, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2001}
print(f"player :{player}")

v = player.values()
print(v)

print("setdefault".center(40, "-"))
player = {'name': 'Rahul', 'runs': 125, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2001}
print(f"player :{player}")

# setdefault is used to add a new key value pair into the dictionary
player.setdefault('oppn', "Aus")
player.setdefault('age', 34)

print(f"Player :{player}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'kol', 'hyd', 'del', 'tvn']
print(f"cities :{cities}")

# convert the list into a dictionary
d1 = dict.fromkeys(cities)
print(f"d1 :{d1}")

print("-" * 40)
d2 = dict.fromkeys(cities, 21)
print(f"d2 :{d2}")


