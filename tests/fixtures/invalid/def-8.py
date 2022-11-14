a = 1  # Check 1
def a():
    pass

def a():  # Check 2
    pass
def a():
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
def a():
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
def a():
    pass

# Check 5
a = """
Multiline string assignment
"""
def a():
    pass

for a in [1, 2]:  # Check 6
    a = 1
    def a():
        pass

for a in [1, 2]:  # Check 7
    def a():
        pass
    def a():
        pass

print(1)  # Check 8
def a():
    pass
