assert 1 == 1  # First line

assert 1 == 1  # Blank line before

# Comment before statement
assert 1 == 1

"""
Multiline comment before statement is ok
"""
assert 1 == 1

if 1 == 1:
    assert 1 == 1
elif 2 == 2:
    assert 1 == 1
else:
    assert 1 == 1


def test():
    assert 1 == 1


try:
    assert 1 == 1
except Exception:
    assert 1 == 1

for a in [1, 2]:
    assert 1 == 1
else:
    assert 1 == 1

while 1 < 2:
    assert 1 == 1
else:
    assert 1 == 1
