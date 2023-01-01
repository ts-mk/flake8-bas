def f():  # Check 3
    v = 1
    # Lorem ipsum dolor sit amet
    yield from [1, 2]

def f():  # Check 4
    v = 1
    """
    Lorem ipsum dolor sit amet
    """
    yield from [1, 2]

def f():  # Check 5
    a = """
    Multiline string assignment
    """
    yield from [1, 2]

def f():  # Check 6
    v = 1
    yield from [1, 2]

def f():  # Check 7
    yield from [1, 2]
    yield from [1, 2]

def f():  # Check 8
    print(1)
    yield from [1, 2]

def f():  # Check 9
    yield from [1, 2]
    print(1)

def f():  # Check 10
    print(1)
    yield from [1, 2]
    print(1)
