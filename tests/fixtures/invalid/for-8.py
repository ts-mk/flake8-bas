a = 1  # Check 1
for a in [1, 2]:
    pass

for a in [1, 2]:  # Check 2
    pass
for a in [1, 2]:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
for a in [1, 2]:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
for a in [1, 2]:
    pass

# Check 5
a = """
Multiline string assignment
"""
for a in [1, 2]:
    pass

for a in [1, 2]:  # Check 6
    a = 1
    for a in [1, 2]:
        pass

for a in [1, 2]:  # Check 7
    for a in [1, 2]:
        pass
    for a in [1, 2]:
        pass

print(1)  # Check 8
for a in [1, 2]:
    pass
