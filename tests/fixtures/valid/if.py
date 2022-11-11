if 1 == 1:  # Check 1
    pass

if 1 == 1:  # Check 2
    pass

"""
Multiline comment before statement is ok
"""
if 1 == 1:  # Check 3
    pass

# Comment before statement
if 1 == 1:  # Check 4
    pass

if 1 == 1:  # Check 5
    if 2 == 2:
        pass
elif 2 == 2:
    if 1 == 1:
        pass
else:
    if 1 == 1:
        pass

for a in [1, 2]:  # Check 6
    if a == 1:
        pass
else:
    if 1 == 1:
        pass

while 1 < 2:  # Check 7
    if 1 == 1:
        pass
else:
    if 1 == 1:
        pass

try: # Check 8
    if 1 == 1:
        pass
except Exception:
    if 1 == 1:
        pass

# Inline if/else should not be affected
b = 1
a = 1 if b == 2 else 0
