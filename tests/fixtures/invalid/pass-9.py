v = 1  # Check 1
pass

pass  # Check 2
pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
pass

a = """
Multiline string assignment
"""
pass  # Check 5

for i in [1, 2]:  # Check 6
    v = 1
    pass

for i in [1, 2]:  # Check 7
    pass
    pass

print(1)  # Check 8
pass

pass  # Check 8
print(1)
