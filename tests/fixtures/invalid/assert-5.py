assert 1 == 1
assert 2 == 2
assert 3 == 3

# Multiline simple statement with blank lines should not affect detection
assert (
    1 == 1

    and

    2 == 2
)
assert 1 == 1

# After simple statement
pass
assert 1 == 1

# After compound statement
if 1 == 1:
    pass
assert 1 == 1
