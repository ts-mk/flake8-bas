a = 1  # Check 1
if 1 == 1:
    pass

if 1 == 1:  # Check 2
    pass
if 1 == 1:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
if 1 == 1:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
if 1 == 1:
    pass

# Check 5
a = """
Multiline string assignment
"""
if 1 == 1:
    pass

for a in [1, 2]:  # Check 6
    a = 1
    if 1 == 1:
        pass

for a in [1, 2]:  # Check 7
    if 1 == 1:
        pass
    if 1 == 1:
        pass

print(1)  # Check 8
if 1 == 1:
    pass
