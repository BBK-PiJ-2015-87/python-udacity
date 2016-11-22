import os
from string import digits

files = os.listdir('./prank')

for f in files:
    remove_digits = str.maketrans('', '', digits)
    res = f.translate(remove_digits)
    print(res)



