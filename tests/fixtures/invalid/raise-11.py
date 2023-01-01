v = 1  # Check 1
raise Exception()

raise Exception()  # Check 2
raise Exception()

v = 1  # Check 3
# Lorem ipsum dolor sit amet
raise Exception()

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
raise Exception()

a = """
Multiline string assignment
"""
raise Exception()  # Check 5

for i in [1, 2]:  # Check 6
    v = 1
    raise Exception()

for i in [1, 2]:  # Check 7
    raise Exception()
    raise Exception()

print(1)  # Check 8
raise Exception()

raise Exception()  # Check 9
print(1)

print(1)  # Check 10
raise Exception()
print(1)
