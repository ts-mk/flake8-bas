a = 1  # Check 1
from os import environ

from os import environ  # Check 2
from os import environ

a = 1  # Check 3
# Lorem ipsum dolor sit amet
from os import environ

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
from os import environ

a = """
Multiline string assignment
"""
from os import environ  # Check 5

for a in [1, 2]:  # Check 6
    a = 1
    from os import environ

for a in [1, 2]:  # Check 7
    from os import environ
    from os import environ

print(1)  # Check 8
from os import environ
