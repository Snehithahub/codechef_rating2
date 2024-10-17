# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    r=0
    arr=list(map(int,input().split()))
    for i in range(2*n):
        if arr[i]>n:
            c=c+1
        else:
            r=r+c
    print(r)        
