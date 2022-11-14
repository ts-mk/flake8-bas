for a in [1, 2]:  # Check 3
    a = 1
    # Lorem ipsum dolor sit amet
    break

for a in [1, 2]:  # Check 4
    a = 1
    """
    Lorem ipsum dolor sit amet
    """
    break

for a in [1, 2]:  # Check 5
    a = """
    Multiline string assignment
    """
    break

for a in [1, 2]:  # Check 6
    a = 1
    break

for a in [1, 2]:  # Check 7
    break
    break

for a in [1, 2]:  # Check 8
    print(1)
    break
