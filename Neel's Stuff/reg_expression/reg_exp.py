# print each line of a text file

f = open('patterns.txt')
line = ""

for i in list(f.read()):
    if i == '\n':
        print(line)
        line = ""
    else:
        line = line + i
print(line)
print(f)