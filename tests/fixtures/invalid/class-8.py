a = 1  # Check 1
class A:
    pass

class A:  # Check 2
    pass
class A:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
class A:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
class A:
    pass

# Check 5
a = """
Multiline string assignment
"""
class A:
    pass

for a in [1, 2]:  # Check 6
    a = 1
    class A:
        pass

for a in [1, 2]:  # Check 7
    class A:
        pass
    class A:
        pass

print(1)  # Check 8
class A:
    pass
