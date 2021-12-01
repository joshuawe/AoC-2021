"""Create all directories
"""

import os

for i in range(1,25):
    name = "Day " + f"{i:02}"
    print(name)
    try:
        os.mkdir(name)
    except OSError as e:
        print(e)