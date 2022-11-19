v = 1  # Check 1
async def f():
    pass

async def f():  # Check 2
    pass
async def f():
    pass

v = 1  # Check 3
# Lorem ipsum dolor sit amet
async def f():
    pass

v = 1  # Check 4
"""
Lorem ipsum dolor sit amet
"""
async def f():
    pass

# Check 5
a = """
Multiline string assignment
"""
async def f():
    pass

for i in [1, 2]:  # Check 6
    v = 1
    async def f():
        pass

for i in [1, 2]:  # Check 7
    async def f():
        pass
    async def f():
        pass

print(1)  # Check 8
async def f():
    pass

async def f():  # Check 9
    pass
print(1)
