for i in [1, 2]:  # Check 1
    pass

for i in [1, 2]:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
for i in [1, 2]:  # Check 3
    pass

# Lorem ipsum dolor sit amet
for i in [1, 2]:  # Check 4
    pass

if 1 == 1:  # Check 5
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
elif 2 == 2:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
else:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass

for i in [1, 2]:  # Check 6
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
else:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass

while True:  # Check 7
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
else:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass

try: # Check 8
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
except Exception:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass
finally:
    for i in [1, 2]:
        pass

    for i in [1, 2]:
        pass

# Comprehension should not be affected
b = 1
a = [i for i in [1, 2]]
