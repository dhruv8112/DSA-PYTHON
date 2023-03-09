def insertion_sort(value):
    length=len(value)
    for i in range(1 ,length):
        point=value[i]
        for j in range(i-1,-1,-1):
            if point >= value[j]:
                break
            value[j+1]=value[j]
        value[j+1]=point
        
        
    
    return(value)

ar=list(map(int,input('ENTER INPUT-->').split()))
print('non sorted array' , ar)

print(insertion_sort(ar))
