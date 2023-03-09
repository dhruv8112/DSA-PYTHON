lst = list(map(int, input().split()))
print(len(lst))
val = int(input())

for i in range(len(lst)):
    if val == lst[i]:
        print('found')
        break
else:
    print('not found')