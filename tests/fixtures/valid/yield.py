def f():
    """
    test
    :return:
    """
    yield 1

def f():  # Check 2
    v = 1

    yield 1

def f():  # Check 3
    v = 1

    """
    Lorem ipsum dolor sit amet
    """
    yield 1

def f():  # Check 4
    v = 1

    # Lorem ipsum dolor sit amet
    yield 1

def f():  # Check 5
    if 1 == 1:
        yield 1

        yield 1
    elif 2 == 2:
        yield 1

        yield 1
    else:
        yield 1

        yield 1


def f():  # Check 8
    try:
        yield 1

        yield 1
    except Exception:
        yield 1

        yield 1
    finally:
        yield 1

        yield 1
