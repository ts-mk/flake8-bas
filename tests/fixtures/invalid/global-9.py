v = 1  # Check 1
global v

global v  # Check 2
global v

v = 1  # Check 3
# Lorem ipsum dolor sit amet
global v

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
global v

# Check 5
a = """
Multiline string assignment
"""
global v

for i in [1, 2]:  # Check 6
    v = 1
    global v

for i in [1, 2]:  # Check 7
    global v
    global v

print(1)  # Check 8
global v

global v  # Check 9
print(1)
