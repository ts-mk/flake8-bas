with f() as b:  # Check 1
    pass

with f() as b:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
with f() as b:  # Check 3
    pass

# Lorem ipsum dolor sit amet
with f() as b:  # Check 4
    pass

if 1 == 1:  # Check 5
    with f() as b:
        pass

    with f() as b:
        pass
elif 2 == 2:
    with f() as b:
        pass

    with f() as b:
        pass
else:
    with f() as b:
        pass

    with f() as b:
        pass

for i in [1, 2]:  # Check 6
    with f() as b:
        pass

    with f() as b:
        pass
else:
    with f() as b:
        pass

    with f() as b:
        pass

while True:  # Check 7
    with f() as b:
        pass

    with f() as b:
        pass
else:
    with f() as b:
        pass

    with f() as b:
        pass

try: # Check 8
    with f() as b:
        pass

    with f() as b:
        pass
except Exception:
    with f() as b:
        pass

    with f() as b:
        pass
