v = 1  # Check 1
def f():
    pass

def f():  # Check 2
    pass
def f():
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
def f():
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
def f():
    pass

# Check 5
a = """
Multiline string assignment
"""
def f():
    pass

for i in [1, 2]:  # Check 6
    v = 1
    def f():
        pass

for i in [1, 2]:  # Check 7
    def f():
        pass
    def f():
        pass

print(1)  # Check 8
def f():
    pass

def f():  # Check 9
    pass
print(1)

print(1)  # Check 10
def f():
    pass
print(1)
