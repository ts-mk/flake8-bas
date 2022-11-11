a = 1  # Check 1
del a

del a  # Check 2
del a

a = 1
# Comment before statement
del a  # Check 3

a = """
Multiline string assignment
"""
del a  # Check 4

for a in [1, 2]:  # Check 5
    a = 1
    del a

for a in [1, 2]:  # Check 6
    del a
    del a
