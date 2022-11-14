def _():  # Check 3
    a = 1
    # Lorem ipsum dolor sit amet
    yield 1

def _():  # Check 4
    a = 1
    """
    Lorem ipsum dolor sit amet
    """
    yield 1

def _():  # Check 5
    a = """
    Multiline string assignment
    """
    yield 1

def _():  # Check 6
    a = 1
    yield 1

def _():  # Check 7
    yield 1
    yield 1

def _():  # Check 8
    print(1)
    yield 1
