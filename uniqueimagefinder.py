#!/usr/bin/env python3

""" 
Photos and videos on an iphone are named using an increment (e.g. 
IMG_0001.HEIC, IMG_0002.HEIC, IMG_0003.MOV). This tool looks at two
directories and lists the set of IMG numbers that are unique, i.e. the IMG 
numbers that do not appear in both sets.
"""

import sys
import os
import re

sets = [(sys.argv[1], set()), (sys.argv[2], set())]
for d, s in sets:
    for f in os.listdir(d):
        # Don't match files with .PNG extension because they're usually screenshots
        # or .AAE files because I don't even know what those files are
        match = re.match("IMG_(\d{4})(?!.PNG|.AAE)", f)
        if match is not None:
            s.add(int(match.group(1)))

unique = list(sets[0][1] ^ sets[1][1])
unique.sort()

for v in unique:
    if v in sets[0][1]:
        print(f"{v} is unique to first directory")
    else:
        print(f"{v} is unique to second directory")
