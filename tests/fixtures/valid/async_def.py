async def f():  # Check 1
    pass

async def f():  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
async def f():  # Check 3
    pass

# Lorem ipsum dolor sit amet
async def f():  # Check 4
    pass

if 1 == 1:  # Check 5
    async def f():
        pass

    async def f():
        pass
elif 2 == 2:
    async def f():
        pass

    async def f():
        pass
else:
    async def f():
        pass

    async def f():
        pass

for i in [1, 2]:  # Check 6
    async def f():
        pass

    async def f():
        pass
else:
    async def f():
        pass

    async def f():
        pass

while True:  # Check 7
    async def f():
        pass

    async def f():
        pass
else:
    async def f():
        pass

    async def f():
        pass

try: # Check 8
    async def f():
        pass

    async def f():
        pass
except Exception:
    async def f():
        pass

    async def f():
        pass
finally:
    async def f():
        pass

    async def f():
        pass
