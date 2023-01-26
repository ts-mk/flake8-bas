def f():
    """
    test
    :return:
    """
    yield from [1, 2]

def f():  # Check 2
    v = 1

    yield from [1, 2]

def f():  # Check 3
    v = 1

    """
    Lorem ipsum dolor sit amet
    """
    yield from [1, 2]

def f():  # Check 4
    v = 1

    # Lorem ipsum dolor sit amet
    yield from [1, 2]

def f():  # Check 5
    if 1 == 1:
        yield from [1, 2]

        yield from [1, 2]
    elif 2 == 2:
        yield from [1, 2]

        yield from [1, 2]
    else:
        yield from [1, 2]

        yield from [1, 2]


def f():  # Check 8
    try:
        yield from [1, 2]

        yield from [1, 2]
    except Exception:
        yield from [1, 2]

        yield from [1, 2]
    finally:
        yield from [1, 2]

        yield from [1, 2]
