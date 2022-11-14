async with a() as b:  # Check 1
    pass

async with a() as b:  # Check 2
    pass

"""
Lorem ipsum dolor sit amet
"""
async with a() as b:  # Check 3
    pass

# Lorem ipsum dolor sit amet
async with a() as b:  # Check 4
    pass

if 1 == 1:  # Check 5
    async with a() as b:
        pass
elif 2 == 2:
    async with a() as b:
        pass
else:
    async with a() as b:
        pass

for a in [1, 2]:  # Check 6
    async with a() as b:
        pass
else:
    async with a() as b:
        pass

while True:  # Check 7
    async with a() as b:
        pass
else:
    async with a() as b:
        pass

try: # Check 8
    async with a() as b:
        pass
except Exception:
    async with a() as b:
        pass
