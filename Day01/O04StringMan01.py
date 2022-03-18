
st = "hello world"
print(f"st :{st}")
print(type(st))

# string are stored like lists
print("-" * 40)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 40)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 40)
# 0 - 4 (<5)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
# by default it gets incremeted by 1 (2 is the increment value)
print(f"st[0:11:2]  :{st[0:11:2]}")
print(f"st[0:11]    :{st[0:11]}")
print(f"st[0:]      :{st[0:]}")
print(f"st[:11]     :{st[:11]}")
print(f"st[:]       :{st[:]}")

# reverse order
print("-" * 40)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# print("-" * 40)
# strings are immutable because str class does not have a setter method
# print(f"st :{st}")
# print(f"st[6] :{st[6]}")
# st[6] = "W"

# print("-" * 40)
# print(dir(st))

print("-" * 40)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.replace("fox", "tiger")
print(f'res :{res}')

res = st.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 40)
res = st.index("the")
print(f"res :{res}")

res = st.index("the", 4)
print(f"res :{res}")

