raise Exception()  # Check 1

raise Exception()  # Check 2

"""
Lorem ipsum dolor sit amet
"""
raise Exception()  # Check 3

# Lorem ipsum dolor sit amet
raise Exception()  # Check 4

if 1 == 1:  # Check 5
    raise Exception()
elif 2 == 2:
    raise Exception()
else:
    raise Exception()

for a in [1, 2]:  # Check 6
    raise Exception()
else:
    raise Exception()

while True:  # Check 7
    raise Exception()
else:
    raise Exception()

try: # Check 8
    raise Exception()
except Exception:
    raise Exception()
