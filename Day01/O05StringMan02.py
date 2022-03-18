
# csv => "101, Jack, MGR, 41, Finance, 145000"
emp = "101, Sameul Jackson, M, MGR, 41, Finance, 145000"
print(f"emp :{emp}")
print(type(emp))

print("-" * 40)
emplst = emp.split(", ")
print(f"emplst :{emplst}")
print(type(emplst))
print(f"Name :{emplst[1]}")
print(f"Dept :{emplst[5]}")

print("-" * 40)
# convert a list back to a string
emp1 = ", ".join(emplst)
print(f"emp1 :{emp1}")
print(type(emp1))

# maketrans and trasnslate
print("-" * 40)
st = "hello world"
print(f"st :{st}")

# convert the string into upper case
a = "helowrd"
b = "HELOWRD"
restbl = st.maketrans(a, b)
print(f"restbl :{restbl}")

res = st.translate(restbl)
print(f"res :{res}")

print("-" * 40)
st = "*****Hello***********"
print(f"st :{st}")
rres = st.rstrip("*")
print(f"rres :{rres}")
lres = st.lstrip("*")
print(f"lres :{lres}")
res = st.strip("*")
print(f"res :{res}")
