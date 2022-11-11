a = 1  # Check 1
assert 1 == 1

assert 1 == 1  # Check 2
assert 1 == 1

a = 1
# Comment before statement
assert 1 == 1  # Check 3

a = """
Multiline string assignment
"""
assert 1 == 1  # Check 4

for a in [1, 2]:  # Check 5
    a = 1
    assert 1 == 1

for a in [1, 2]:  # Check 6
    assert 1 == 1
    assert 1 == 1
