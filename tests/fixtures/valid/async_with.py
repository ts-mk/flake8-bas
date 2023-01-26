async with f() as b:  # Check 1
    pass

async with f() as b:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
async with f() as b:  # Check 3
    pass

# Lorem ipsum dolor sit amet
async with f() as b:  # Check 4
    pass

if 1 == 1:  # Check 5
    async with f() as b:
        pass

    async with f() as b:
        pass
elif 2 == 2:
    async with f() as b:
        pass

    async with f() as b:
        pass
else:
    async with f() as b:
        pass

    async with f() as b:
        pass

for i in [1, 2]:  # Check 6
    async with f() as b:
        pass

    async with f() as b:
        pass
else:
    async with f() as b:
        pass

    async with f() as b:
        pass

while True:  # Check 7
    async with f() as b:
        pass

    async with f() as b:
        pass
else:
    async with f() as b:
        pass

    async with f() as b:
        pass

try: # Check 8
    async with f() as b:
        pass

    async with f() as b:
        pass
except Exception:
    async with f() as b:
        pass

    async with f() as b:
        pass
finally:
    async with f() as b:
        pass

    async with f() as b:
        pass
