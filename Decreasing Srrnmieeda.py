# cook your dish here
for i in range(int(input())):
    l,r=map(int,input().split())
    if l>=(r-l+1):
        print(r)
    else:
        print(-1)
