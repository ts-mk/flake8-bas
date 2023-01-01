v = 1  # Check 1
match True:
    case True:
        pass

match True:  # Check 2
    case True:
        pass
match True:
    case True:
        pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
match True:
    case True:
        pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
match True:
    case True:
        pass

a = """
Multiline string assignment
"""
match True:  # Check 5
    case True:
        pass

for i in [1, 2]:  # Check 6
    v = 1
    match True:
        case True:
            pass

for i in [1, 2]:  # Check 7
    match True:
        case True:
            pass
    match True:
        case True:
            pass

print(1)  # Check 8
match True:
    case True:
        pass

match True:  # Check 9
    case True:
        pass
print(1)

print(1)  # Check 10
match True:
    case True:
        pass
print(1)
