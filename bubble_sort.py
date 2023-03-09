def bubble_sort(indexx):
    leg=len(indexx)
    print('SIZE OF INDEX -->' ,leg)
    swap=0

    for i in range(leg-1):
        pos=i
        print(i)
        for j in range (0,leg-1):
            if indexx[j] > indexx[j+1] :
                indexx[j], indexx[j+1] = indexx[j+1], indexx[j]
                swap+=1
                print('INDEX-->' ,indexx)
 
    return indexx



ar=list(map(int,input('ENTER INPUT-->').split()))
print('NON-SORTED ARRAY IS','\n',ar)

print(bubble_sort(ar))