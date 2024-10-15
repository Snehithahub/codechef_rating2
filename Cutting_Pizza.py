from math import gcd
from functools import reduce
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    d=[]
    for i in range(1,n):
        d.append((arr[i]-arr[i-1]))
    d.append(360-arr[-1]+arr[0])  
    x=reduce(gcd,d)
    print((360//x)-n)
