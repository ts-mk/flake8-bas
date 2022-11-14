class A:  # Check 1
    pass

class A:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
class A:  # Check 3
    pass

# Lorem ipsum dolor sit amet
class A:  # Check 4
    pass

if 1 == 1:  # Check 5
    class A:
        pass
elif 2 == 2:
    class A:
        pass
else:
    class A:
        pass

for a in [1, 2]:  # Check 6
    class A:
        pass
else:
    class A:
        pass

while True:  # Check 7
    class A:
        pass
else:
    class A:
        pass

try: # Check 8
    class A:
        pass
except Exception:
    class A:
        pass
