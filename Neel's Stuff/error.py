l = []
i = 0

def stack(a):
    while i <= 1000:
        l.append(1)
        stack(a)

stack(10)