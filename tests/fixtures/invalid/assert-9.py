v = 1  # Check 1
assert 1 == 1

assert 1 == 1  # Check 2
assert 1 == 1

v = 1  # Check 3
# Lorem ipsum dolor sit amet
assert 1 == 1

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
assert 1 == 1

a = """
Multiline string assignment
"""
assert 1 == 1  # Check 5

for i in [1, 2]:  # Check 6
    v = 1
    assert 1 == 1

for i in [1, 2]:  # Check 7
    assert 1 == 1
    assert 1 == 1

print(1)  # Check 8
assert 1 == 1

assert 1 == 1  # Check 9
print(1)
