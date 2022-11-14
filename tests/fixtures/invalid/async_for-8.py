a = 1  # Check 1
async for a in [1, 2]:
    pass

async for a in [1, 2]:  # Check 2
    pass
async for a in [1, 2]:
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
async for a in [1, 2]:
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async for a in [1, 2]:
    pass

# Check 5
a = """
Multiline string assignment
"""
async for a in [1, 2]:
    pass

async for a in [1, 2]:  # Check 6
    a = 1
    async for a in [1, 2]:
        pass

async for a in [1, 2]:  # Check 7
    async for a in [1, 2]:
        pass
    async for a in [1, 2]:
        pass

print(1)  # Check 8
async for a in [1, 2]:
    pass
