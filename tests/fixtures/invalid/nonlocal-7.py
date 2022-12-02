def f():  # Check 3
    v = 1
    # Lorem ipsum dolor sit amet
    nonlocal b

def f():  # Check 4
    v = 1
    """
    Lorem ipsum dolor sit amet
    """
    nonlocal b

def f():  # Check 5
    a = """
    Multiline string assignment
    """
    nonlocal b

def f():  # Check 6
    v = 1
    nonlocal b

def f():  # Check 7
    nonlocal b
    nonlocal b

def f():  # Check 8
    print(1)
    nonlocal b

def f():  # Check 9
    nonlocal b
    print(1)
