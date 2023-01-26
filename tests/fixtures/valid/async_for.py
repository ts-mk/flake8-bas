async for i in [1, 2]:  # Check 1
    pass

async for i in [1, 2]:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
async for i in [1, 2]:  # Check 3
    pass

# Lorem ipsum dolor sit amet
async for i in [1, 2]:  # Check 4
    pass

if 1 == 1:  # Check 5
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
elif 2 == 2:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
else:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass

async for i in [1, 2]:  # Check 6
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
else:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass

while True:  # Check 7
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
else:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass

try: # Check 8
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
except Exception:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
finally:
    async for i in [1, 2]:
        pass

    async for i in [1, 2]:
        pass
