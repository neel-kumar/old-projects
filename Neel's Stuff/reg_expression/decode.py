import re

st = """
4
4.0O0
-1.00
+4.54
SomeRandomStuff
"""
line = re.compile(r'.+\n')
lines = line.finditer(st)

first_line = True

for l in lines:
    if not first_line:
        pattern = re.compile(r'\d*\.\d+\n')
        matches = pattern.finditer(l.group(0))
        i = 0
        for match in matches:
            i = i + 1
            print('True')
        if i == 0:
            print("False")
    
    # Do your processing
    first_line = False
