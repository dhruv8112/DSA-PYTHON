def sel_Sort(value):
    ln = len(value)
    print('Element in the list ',ln)
    if ln == 0:
        print('Empty elemnt')
    else:
        print('TOtal round will be performed', ln-1)
    swap = 0
    round = 0
    for i in range(ln-1):
        pos = i
        for j in range(i+1, ln):
            if value[j] < value[pos]:
                pos = j

        if value[pos] != i:
            value[i], value[pos] = value[pos], value[i]
            swap += 1
        round += 1
        print('ROUND', round, value)
    return value


ar = list(map(int, input('Enter value-->').split()))
print(ar)
print('SORTED','\n',sel_Sort(ar))