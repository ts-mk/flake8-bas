a = 1  # Check 1
del a

del a  # Check 2
del a

a = 1  # Check 3
# Lorem ipsum dolor sit amet
del a

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
del a

a = """
Multiline string assignment
"""
del a  # Check 5

for a in [1, 2]:  # Check 6
    a = 1
    del a

for a in [1, 2]:  # Check 7
    del a
    del a

print(1)  # Check 8
del a
