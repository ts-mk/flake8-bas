def _():
    """
    test
    :return:
    """
    yield from [1, 2]

def _():  # Check 2
    a = 1

    yield from [1, 2]

def _():  # Check 3
    a = 1

    """
    Lorem ipsum dolor sit amet
    """
    yield from [1, 2]

def _():  # Check 4
    a = 1

    # Lorem ipsum dolor sit amet
    yield from [1, 2]

def _():  # Check 5
    if 1 == 1:
        yield from [1, 2]
    elif 2 == 2:
        yield from [1, 2]
    else:
        yield from [1, 2]


def _():  # Check 8
    try:
        yield from [1, 2]
    except Exception:
        yield from [1, 2]
