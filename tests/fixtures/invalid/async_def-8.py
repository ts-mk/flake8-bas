a = 1  # Check 1
async def a():
    pass

async def a():  # Check 2
    pass
async def a():
    pass

a = 1  # Check 3
# Lorem ipsum dolor sit amet
async def a():
    pass

a = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async def a():
    pass

# Check 5
a = """
Multiline string assignment
"""
async def a():
    pass

for a in [1, 2]:  # Check 6
    a = 1
    async def a():
        pass

for a in [1, 2]:  # Check 7
    async def a():
        pass
    async def a():
        pass

print(1)  # Check 8
async def a():
    pass
