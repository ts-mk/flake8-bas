global a  # Check 1

global a  # Check 2

"""
Lorem ipsum dolor sit amet
"""
global a  # Check 3

# Lorem ipsum dolor sit amet
global a  # Check 4

if 1 == 1:  # Check 5
    global a

    global a
elif 2 == 2:
    global a

    global a
else:
    global a

    global a

for i in [1, 2]:  # Check 6
    global a

    global a
else:
    global a

    global a

while True:  # Check 7
    global a

    global a
else:
    global a

    global a

try: # Check 8
    global a

    global a
except Exception:
    global a

    global a
