for a in range(10):  # Check 2
    a = 1

    continue

for a in range(10):  # Check 3
    """
    Multiline comment before statement is ok
    """
    continue

for a in range(10):  # Check 4
    a = 1

    # Comment before statement
    continue

for a in range(10):  # Check 5
    if 1 == 1:
        continue
    elif 2 == 2:
        continue
    else:
        continue

try: # Check 8
    for a in range(10):
        continue
except Exception:
    for a in range(10):
        continue
