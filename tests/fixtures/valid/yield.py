def _():
    """
    test
    :return:
    """
    yield 1

def _():  # Check 2
    a = 1

    yield 1

def _():  # Check 3
    a = 1

    """
    Lorem ipsum dolor sit amet
    """
    yield 1

def _():  # Check 4
    a = 1

    # Lorem ipsum dolor sit amet
    yield 1

def _():  # Check 5
    if 1 == 1:
        yield 1
    elif 2 == 2:
        yield 1
    else:
        yield 1


def _():  # Check 8
    try:
        yield 1
    except Exception:
        yield 1
