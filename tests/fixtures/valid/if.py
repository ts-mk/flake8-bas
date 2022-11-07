if 1 == 1:  # First line
    pass

if 1 == 1:  # Blank line before
    pass

# Comment before statement
if 1 == 1:
    pass

"""
Multiline comment before statement is ok
"""
if 1 == 1:
    pass

if 1 == 1:
    if 2 == 2:
        pass
elif 2 == 2:
    if 1 == 1:
        pass
else:
    if 1 == 1:
        pass

# Inline if/else is not affected
b = 1
a = 1 if b == 2 else 0

try:
    if 1 == 1:
        pass
except Exception:
    if 1 == 1:
        pass

for a in [1, 2]:
    if a == 1:
        pass
else:
    if 1 == 1:
        pass


def test():
    if 1 == 1:
        pass


class Test:
    if 1 == 1:
        pass


while 1 < 2:
    if 1 == 1:
        pass
else:
    if 1 == 1:
        pass
