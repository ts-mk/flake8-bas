def f():
    """
    test
    :return:
    """
    nonlocal v

def f():  # Check 2
    v = 1

    nonlocal v

def f():  # Check 3
    v = 1

    """
    Lorem ipsum dolor sit amet
    """
    nonlocal v

def f():  # Check 4
    v = 1

    # Lorem ipsum dolor sit amet
    nonlocal v

def f():  # Check 5
    if 1 == 1:
        nonlocal v

        nonlocal v
    elif 2 == 2:
        nonlocal v

        nonlocal v
    else:
        nonlocal v

        nonlocal v


def f():  # Check 8
    try:
        nonlocal v

        nonlocal v
    except Exception:
        nonlocal v

        nonlocal v
    finally:
        nonlocal v

        nonlocal v
