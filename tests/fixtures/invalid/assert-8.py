a = 1  # Check 1
assert 1 == 1

assert 1 == 1  # Check 2
assert 1 == 1

a = 1  # Check 3
# Lorem ipsum dolor sit amet
assert 1 == 1

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
assert 1 == 1

a = """
Multiline string assignment
"""
assert 1 == 1  # Check 5

for a in [1, 2]:  # Check 6
    a = 1
    assert 1 == 1

for a in [1, 2]:  # Check 7
    assert 1 == 1
    assert 1 == 1

print(1)  # Check 8
assert 1 == 1
