def _():  # Check 3
    a = 1
    # Lorem ipsum dolor sit amet
    nonlocal b

def _():  # Check 4
    a = 1
    """
    Lorem ipsum dolor sit amet
    """
    nonlocal b

def _():  # Check 5
    a = """
    Multiline string assignment
    """
    nonlocal b

def _():  # Check 6
    a = 1
    nonlocal b

def _():  # Check 7
    nonlocal b
    nonlocal b

def _():  # Check 8
    print(1)
    nonlocal b
