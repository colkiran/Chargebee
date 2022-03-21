
"""
1. sort
2. sorted

sort will sort the original list
sorted will return a copy of the sorted list
"""

print("sort".center(40,"-"))
l1 = [10, 4, 9, 7, 2, 8, 5, 1, 6, 3]
print(f"l1 :{l1}")

res1 = sorted(l1)
print(f"res1 :{res1}")
res2 = sorted(l1, reverse=True)
print(f"res2 :{res2}")

print("-" * 40)
l1 = [10,'zebra', 4,'apple', 'yellow',  9, 'xmas', 'ball',  7, 'pink', 'cat', 2, 'orange',
      'maroon', 8, 'frog', 'violet', 5, 'rose', 1, 'lilly', 6, 'sunflower', 3, 19, 125, 1050,
      27, 213, 2282]

print(f"l1 :{l1}")
res = sorted(l1, key=ascii)
print("-" * 40)
print(f"res :{res}")

print("-" * 40)
cities = ['vishakapatnam', 'bangalore', 'pune', 'mysore', 'delhi', 'thiruvananthapuram',
          'hyderabad', 'kanyakumari', 'ooty', 'madurai', 'mumbai']
print(f"cities :{cities}")
print("-" * 40)

res = sorted(cities,key=len)
print(f"res :{res}")

print("-" * 40)
cities.sort(key=len, reverse=True)
print(f"cities :{cities}")

months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']

# sort the months according to the calendar

print("reversed".center(40, "-"))
l1 = [10, 4, 9, 7, 2, 8, 5, 1, 6, 3]
print(f"l1 :{l1}")

print("-" * 40)
res = list(reversed(l1))
print(f"res :{res}")

print("clear".center(40, "-"))
l1 = [10, 4, 9, 7, 2, 8, 5, 1, 6, 3]
print(f"l1 Before :{l1}")

l1.clear()
print(f"l1 After :{l1}")
