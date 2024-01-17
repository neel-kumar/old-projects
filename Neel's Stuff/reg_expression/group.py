import re

pattern = re.compile(r'([a-zA-Z0-9])\1')
matches = pattern.search(input())

if matches == None:
    print("-1")
else:
    print(matches.group(1))