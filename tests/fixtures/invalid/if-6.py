a = 1  # Check 1
if 1 == 1:
    pass

if 1 == 1:  # Check 2
    pass
if 1 == 1:
    pass

a = 1
# Comment before statement
if a == 1:  # Check 3
    pass

a = """
Multiline string assignment
"""
if a == 1:  # Check 4
    pass

for a in [1, 2]:  # Check 5
    a = 1
    if a == 1:
        pass

for a in [1, 2]:  # Check 6
    if a == 1:
        pass
    if a == 1:
        pass
