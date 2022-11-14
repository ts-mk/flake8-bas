a = 1  # Check 1
raise Exception()

raise Exception()  # Check 2
raise Exception()

a = 1  # Check 3
# Lorem ipsum dolor sit amet
raise Exception()

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
raise Exception()

a = """
Multiline string assignment
"""
raise Exception()  # Check 5

for a in [1, 2]:  # Check 6
    a = 1
    raise Exception()

for a in [1, 2]:  # Check 7
    raise Exception()
    raise Exception()

print(1)  # Check 8
raise Exception()
