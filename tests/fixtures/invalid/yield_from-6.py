def _():  # Check 3
    a = 1
    # Lorem ipsum dolor sit amet
    yield from [1, 2]

def _():  # Check 4
    a = 1
    """
    Lorem ipsum dolor sit amet
    """
    yield from [1, 2]

def _():  # Check 5
    a = """
    Multiline string assignment
    """
    yield from [1, 2]

def _():  # Check 6
    a = 1
    yield from [1, 2]

def _():  # Check 7
    yield from [1, 2]
    yield from [1, 2]

def _():  # Check 8
    print(1)
    yield from [1, 2]
