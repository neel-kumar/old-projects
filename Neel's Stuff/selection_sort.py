def selection_sort(a):
    i = 0
    least = a[i]
    move = 0
    for b in a:
        for i in range(move, len(a)-1):
            if a[i] < a[i+1]:
                least = i
            else:
                least = i+1
        a[move] = a[least]
        a[least] = a[move]
        move = move + 1
    print(a)

selection_sort([5,4,3,2,1])
