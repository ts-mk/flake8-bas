for a in range(10):  # Check 2
    a = 1

    break

for a in range(10):  # Check 3
    """
    Lorem ipsum dolor sit amet
    """
    break

for a in range(10):  # Check 4
    a = 1

    # Lorem ipsum dolor sit amet
    break

for a in range(10):  # Check 5
    if 1 == 1:
        break
    elif 2 == 2:
        break
    else:
        break

try: # Check 8
    for a in range(10):
        break
except Exception:
    for a in range(10):
        break
