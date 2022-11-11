del a  # Check 1

del a  # Check 2

"""
Multiline comment before statement is ok
"""
del a  # Check 3

# Comment before statement
del a  # Check 4

if 1 == 1:  # Check 5
    del a
elif 2 == 2:
    del a
else:
    del a

for a in [1, 2]:  # Check 6
    del a
else:
    del a

while 1 < 2:  # Check 7
    del a
else:
    del a

try: # Check 8
    del a
except Exception:
    del a
