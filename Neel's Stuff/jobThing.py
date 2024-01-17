def jobThing(l):
    seq = []
    fin = []
    seq_var = l[0]
    i = 0
    while(i < len(l)):
        if seq_var < l[i] or len(seq) == 0:
            seq_var = l[i]
            seq.append(seq_var)
            i = i + 1
        else:
            fin.append(seq)
            seq = []
    fin.append(seq)
    seq = []
    print(max(fin))

def max(li):
    max = len(li[0])
    i = 0
    while(i < len(li)):
        if len(li[i]) > max:
            max = len(li[i])
        i = i + 1
    return max

jobThing([1,2,3,2,3,4,5])
#jobThing([1])
#jobThing([1,0,3])
