def _():
    """
    test
    :return:
    """
    nonlocal b

def _():  # Check 2
    a = 1

    nonlocal b

def _():  # Check 3
    a = 1

    """
    Lorem ipsum dolor sit amet
    """
    nonlocal b

def _():  # Check 4
    a = 1

    # Lorem ipsum dolor sit amet
    nonlocal b

def _():  # Check 5
    if 1 == 1:
        nonlocal b
    elif 2 == 2:
        nonlocal b
    else:
        nonlocal b


def _():  # Check 8
    try:
        nonlocal b
    except Exception:
        nonlocal b
