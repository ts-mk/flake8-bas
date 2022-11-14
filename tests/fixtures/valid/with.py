with a() as b:  # Check 1
    pass

with a() as b:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
with a() as b:  # Check 3
    pass

# Lorem ipsum dolor sit amet
with a() as b:  # Check 4
    pass

if 1 == 1:  # Check 5
    with a() as b:
        pass
elif 2 == 2:
    with a() as b:
        pass
else:
    with a() as b:
        pass

for a in [1, 2]:  # Check 6
    with a() as b:
        pass
else:
    with a() as b:
        pass

while True:  # Check 7
    with a() as b:
        pass
else:
    with a() as b:
        pass

try: # Check 8
    with a() as b:
        pass
except Exception:
    with a() as b:
        pass
