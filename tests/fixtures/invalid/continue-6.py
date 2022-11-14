for a in [1, 2]:  # Check 3
    a = 1
    # Lorem ipsum dolor sit amet
    continue

for a in [1, 2]:  # Check 4
    a = 1
    """
    Lorem ipsum dolor sit amet
    """
    continue

for a in [1, 2]:  # Check 5
    a = """
    Multiline string assignment
    """
    continue

for a in [1, 2]:  # Check 6
    a = 1
    continue

for a in [1, 2]:  # Check 7
    continue
    continue

for a in [1, 2]:  # Check 8
    print(1)
    continue
