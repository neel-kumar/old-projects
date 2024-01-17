import re

csv = """
Plain, Text,,,
Cursive, is, Cool,,
Better, than, Plain, Text,
""" 
pattern = re.compile(r'(.+)\n')
matches = pattern.finditer(csv)
subbed_csv = pattern.sub(r'\1', csv)
ii = 0

for match in matches:
    ii = ii + 1
    line = match.group(1)
    pat = re.compile(r'((\d|\w)*),')
    m = pat.finditer(line)
    i = 0
    for mat in m:
        i = i + 1
        print(ii, i, mat.group(1))
    print("\n")
