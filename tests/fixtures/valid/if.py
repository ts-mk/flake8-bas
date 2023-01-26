if 1 == 1:  # Check 1
    pass

if 1 == 1:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
if 1 == 1:  # Check 3
    pass

# Lorem ipsum dolor sit amet
if 1 == 1:  # Check 4
    pass

if 1 == 1:  # Check 5
    if 2 == 2:
        pass

    if 2 == 2:
        pass
elif 2 == 2:
    if 1 == 1:
        pass

    if 2 == 2:
        pass
else:
    if 1 == 1:
        pass

    if 2 == 2:
        pass

for i in [1, 2]:  # Check 6
    if 1 == 1:
        pass

    if 2 == 2:
        pass
else:
    if 1 == 1:
        pass

    if 2 == 2:
        pass

while True:  # Check 7
    if 1 == 1:
        pass

    if 2 == 2:
        pass
else:
    if 1 == 1:
        pass

    if 2 == 2:
        pass

try: # Check 8
    if 1 == 1:
        pass

    if 2 == 2:
        pass
except Exception:
    if 1 == 1:
        pass

    if 2 == 2:
        pass
finally:
    if 1 == 1:
        pass

    if 2 == 2:
        pass

# Inline if/else should not be affected
b = 1
v = 1 if b == 2 else 0
