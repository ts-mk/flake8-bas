v = 1  # Check 1
with f() as b:
    pass

with f() as b:  # Check 2
    pass
with f() as b:
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
with f() as b:
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
with f() as b:
    pass

# Check 5
a = """
Multiline string assignment
"""
with f() as b:
    pass

with f() as b:  # Check 6
    v = 1
    with f() as b:
        pass

with f() as b:  # Check 7
    with f() as b:
        pass
    with f() as b:
        pass

print(1)  # Check 8
with f() as b:
    pass

with f() as b:  # Check 9
    pass
print(1)
