

print("pop".center(40, "-"))
player = {'name': 'Rahul', 'runs': 125, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2001}
print(f"player :{player}")

res = player.pop("venue")
print(f"res :{res}")
print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'Rahul', 'runs': 125, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2001}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

print("items".center(40, "-"))

emp = {
    'emp1': {'name': 'Mike', 'age': 32, 'desig': 'MGR', 'dept':'finance', 'sal': 85000},
    'emp2': {'name': 'Jack', 'age': 28, 'desig': 'BDE', 'dept':'MKT', 'sal': 25000},
    'emp3': {'name': 'Jane', 'age': 30, 'desig': 'Ana', 'dept':'IT', 'sal': 130000}
}

print(f'emp :{emp}')

print("-" * 40)

print(f"emp['emp1'] :{emp['emp1']}")
print(f"emp['emp2'] :{emp['emp2']}")
print(f"emp['emp3'] :{emp['emp3']}")

print("-" * 40)

# items => combination of keys and values
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40,"-"))

emp1 = {'name': 'Mike', 'age': 32, 'desig': 'MGR', 'sal': 85000}            # target
emp2 = {'name': 'Jack', 'age': 28, 'desig': 'BDE', 'dept':'MKT'}            # source

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 32, 'desig': 'MGR', 'dept': 'finance', 'sal': 85000}
print(f"emp1 before :{emp1}")
emp1.clear()

print(f"emp1 after :{emp1}")