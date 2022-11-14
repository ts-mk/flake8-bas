async def a():  # Check 1
    pass

async def a():  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
async def a():  # Check 3
    pass

# Lorem ipsum dolor sit amet
async def a():  # Check 4
    pass

if 1 == 1:  # Check 5
    async def a():
        pass
elif 2 == 2:
    async def a():
        pass
else:
    async def a():
        pass

for a in [1, 2]:  # Check 6
    async def a():
        pass
else:
    async def a():
        pass

while True:  # Check 7
    async def a():
        pass
else:
    async def a():
        pass

try: # Check 8
    async def a():
        pass
except Exception:
    async def a():
        pass
