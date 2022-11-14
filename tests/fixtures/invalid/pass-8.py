a = 1  # Check 1
pass

pass  # Check 2
pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
pass

a = """
Multiline string assignment
"""
pass  # Check 5

for a in [1, 2]:  # Check 6
    a = 1
    pass

for a in [1, 2]:  # Check 7
    pass
    pass

print(1)  # Check 8
pass
