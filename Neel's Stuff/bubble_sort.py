def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            print(j)
            if a[j] > a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
    print(a)

bubble_sort([5,4,3,2,1])
