a = 1  # Check 1
global a

global a  # Check 2
global a

a = 1  # Check 3
# Lorem ipsum dolor sit amet
global a

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
global a

# Check 5
a = """
Multiline string assignment
"""
global a

for a in [1, 2]:  # Check 6
    a = 1
    global a

for a in [1, 2]:  # Check 7
    global a
    global a

print(1)  # Check 8
global a
