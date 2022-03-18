"""
for loop => for each loop => rely on a collection
iterates depending on the number of elements in the collection
range(1, 10)    => 1, 2, 3,4,......9

print(data, sep=, end="\n")
"""
i = 0

for i in range(1, 10):
    print (i, end=" ")
print()

print(f"After :{i}")

i = 10
while i > 0:
    print(i, end=" ")
    i -= 1
print()


