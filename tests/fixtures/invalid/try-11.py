v = 1  # Check 1
try:
    pass
except:
    pass

try:  # Check 2
    pass
except:
    pass
try:
    pass
except:
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
try:
    pass
except:
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
try:
    pass
except:
    pass

a = """
Multiline string assignment
"""
try:  # Check 5
    pass
except:
    pass

for i in [1, 2]:  # Check 6
    v = 1
    try:
        pass
    except:
        pass

for i in [1, 2]:  # Check 7
    try:
        pass
    except:
        pass
    try:
        pass
    except:
        pass

print(1)  # Check 8
try:
    pass
except:
    pass

try:  # Check 9
    pass
except:
    pass
print(1)

print(1)  # Check 10
try:
    pass
except:
    pass
print(1)
