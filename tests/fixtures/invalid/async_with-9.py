v = 1  # Check 1
async with f() as b:
    pass

async with f() as b:  # Check 2
    pass
async with f() as b:
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
async with f() as b:
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async with f() as b:
    pass

# Check 5
a = """
Multiline string assignment
"""
async with f() as b:
    pass

async with f() as b:  # Check 6
    v = 1
    async with f() as b:
        pass

async with f() as b:  # Check 7
    async with f() as b:
        pass
    async with f() as b:
        pass

print(1)  # Check 8
async with f() as b:
    pass

async with f() as b:  # Check 9
    pass
print(1)
