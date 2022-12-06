v = 1  # Check 1
class C:
    pass

class C:  # Check 2
    pass
class C:
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
class C:
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
class C:
    pass

# Check 5
a = """
Multiline string assignment
"""
class C:
    pass

for i in [1, 2]:  # Check 6
    v = 1
    class C:
        pass

for i in [1, 2]:  # Check 7
    class C:
        pass
    class C:
        pass

print(1)  # Check 8
class C:
    pass

class C:  # Check 9
    pass
print(1)

print(1)  # Check 10
class C:
    pass
print(1)
