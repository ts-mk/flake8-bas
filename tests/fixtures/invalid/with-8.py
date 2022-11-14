a = 1  # Check 1
with a() as b:
    pass

with a() as b:  # Check 2
    pass
with a() as b:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
with a() as b:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
with a() as b:
    pass

# Check 5
a = """
Multiline string assignment
"""
with a() as b:
    pass

with a() as b:  # Check 6
    a = 1
    with a() as b:
        pass

with a() as b:  # Check 7
    with a() as b:
        pass
    with a() as b:
        pass

print(1)  # Check 8
with a() as b:
    pass
