v = 1  # Check 1
del a

del a  # Check 2
del a

v = 1  # Check 3
# Lorem ipsum dolor sit amet
del a

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
del a

a = """
Multiline string assignment
"""
del a  # Check 5

for i in [1, 2]:  # Check 6
    v = 1
    del a

for i in [1, 2]:  # Check 7
    del a
    del a

print(1)  # Check 8
del a

del a  # Check 9
print(1)
