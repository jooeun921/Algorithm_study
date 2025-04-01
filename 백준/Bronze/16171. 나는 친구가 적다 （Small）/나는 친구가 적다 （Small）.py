from sys import stdin
import re

note = str(stdin.readline())
note = re.sub(r'[0-9]', '', note)
ans = str(stdin.readline())

if ans in note:
    print(1)
else:
    print(0)