import re

#s = input()
#p = input()
s = "a"
pattern = re.compile(s)
start = 0
i = 0

while True:
    match = pattern.search("aaadaa", pos = start)
    if match == None:
        break
    i = i + 1
    t = (match.start(), (match.end() - 1),)
    # print("(",match.start(),", ",(match.end() - 1),")")
    print(t)
    if len(s) == 1:
        start = match.end()
    else:
        start = match.end() - 1


if i == 0:
    print("(-1, -1)")
