def twosum(ar, target):
    pair=[]
    for i in range(len(ar)):
        ans = target - ar[i]
        if ans in ar:
            a=ar[i], ans
            pair.append(a)
    if pair:
        for i in pair:
            print("The numbers that add up to", target, "=", i[0], "+", i[1])
    else:
        print("No numbers in the array add up to", target, ".")
    print('PAIR--> ', pair)
    
ar = list(map(int, input('Enter Array-->').split()))
print('ARRAY' , ar)

target = int(input('Enter sum-->'))

twosum(ar, target)
