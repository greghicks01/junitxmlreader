import os
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


files = [f for f in os.listdir('.') if os.path.isfile(f)]

for file in [f for f in os.listdir('.') if os.path.isfile(f)]:
    print(f'file name is {file}')

print('normal', file=sys.stdout)
eprint('this better go to error')
