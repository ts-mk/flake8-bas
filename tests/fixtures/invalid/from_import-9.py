v = 1  # Check 1
from os import environ

from os import environ  # Check 2
from os import environ

v = 1  # Check 3
# Lorem ipsum dolor sit amet
from os import environ

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
from os import environ

a = """
Multiline string assignment
"""
from os import environ  # Check 5

for i in [1, 2]:  # Check 6
    v = 1
    from os import environ

for i in [1, 2]:  # Check 7
    from os import environ
    from os import environ

print(1)  # Check 8
from os import environ

from os import environ  # Check 9
print(1)
