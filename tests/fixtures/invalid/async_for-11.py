v = 1  # Check 1
async for i in [1, 2]:
    pass

async for i in [1, 2]:  # Check 2
    pass
async for i in [1, 2]:
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
async for i in [1, 2]:
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async for i in [1, 2]:
    pass

# Check 5
a = """
Multiline string assignment
"""
async for i in [1, 2]:
    pass

async for i in [1, 2]:  # Check 6
    v = 1
    async for i in [1, 2]:
        pass

async for i in [1, 2]:  # Check 7
    async for i in [1, 2]:
        pass
    async for i in [1, 2]:
        pass

print(1)  # Check 8
async for i in [1, 2]:
    pass

async for i in [1, 2]:  # Check 9
    pass
print(1)

print(1)  # Check 10
async for i in [1, 2]:
    pass
print(1)
