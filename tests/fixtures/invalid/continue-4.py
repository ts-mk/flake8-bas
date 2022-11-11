for a in [1, 2]:  # Check 3
    a = 1
    # Comment before statement
    continue

for a in [1, 2]:  # Check 4
    a = """
    Multiline string assignment
    """
    continue

for a in [1, 2]:  # Check 5
    a = 1
    continue

for a in [1, 2]:  # Check 6
    continue
    continue
