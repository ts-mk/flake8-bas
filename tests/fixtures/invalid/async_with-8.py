a = 1  # Check 1
async with a() as b:
    pass

async with a() as b:  # Check 2
    pass
async with a() as b:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
async with a() as b:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async with a() as b:
    pass

# Check 5
a = """
Multiline string assignment
"""
async with a() as b:
    pass

async with a() as b:  # Check 6
    a = 1
    async with a() as b:
        pass

async with a() as b:  # Check 7
    async with a() as b:
        pass
    async with a() as b:
        pass

print(1)  # Check 8
async with a() as b:
    pass
