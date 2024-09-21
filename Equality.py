# cook your dish here

for _ in range(int(input())):
    n = int(input())
    
    arr = list(map(int,input().split()))
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    s=int(sum/(n-1))
    for j in range(n):
       print(s-arr[j], end=" ")
    print('')
