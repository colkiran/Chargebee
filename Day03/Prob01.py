
from calendar import month_name

print(list(month_name))

for m in list(month_name):
    print(m[0:3].lower(), end=" ")
print()

print("-" * 40)
months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']
print(f"months :{months}")

l = list(range(1, 11))
print(f"l :{l}")

def square(n):
    return n ** 2

res = list(map(square, l))
print(f"res :{res}")

# lambda var1, var2..: expression

print("=" * 40)
def monthName(mon):
    l = []
    for m in list(month_name):
        l.append(str(m[0:3].lower()))
    if mon in l:
        return l.index(mon)


# print(monthName("feb"))
# srtdMon = sorted(months, key=list(map(lambda m: m[0:3].lower(), list(month_name))).index)
months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']
srtdMon = sorted(months, key=monthName)
print(f"Sorted Months :{srtdMon}")



