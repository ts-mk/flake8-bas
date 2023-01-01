def f():  # Check 3
    v = 1
    # Lorem ipsum dolor sit amet
    yield 1

def f():  # Check 4
    v = 1
    """
    Lorem ipsum dolor sit amet
    """
    yield 1

def f():  # Check 5
    a = """
    Multiline string assignment
    """
    yield 1

def f():  # Check 6
    v = 1
    yield 1

def f():  # Check 7
    yield 1
    yield 1

def f():  # Check 8
    print(1)
    yield 1

def f():  # Check 9
    yield 1
    print(1)

def f():  # Check 10
    print(1)
    yield 1
    print(1)
