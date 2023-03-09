def selection_sort(arr):
    n = len(arr)
    print(n)
    swap=0
    for i in range(n-1):

        min_index = i
        print(min_index)
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if arr[min_index]!=i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap+=1
    print(swap)
    return arr





ar = map(int, input().split())


lst = list(ar)


print(lst)
a=selection_sort(lst)
print(a)
