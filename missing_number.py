n = int(input())
list =[int(i) for i in input().split()]
for i in range(1,n+1):
    if i in list:
        None
    else:
        print(i)
        break
