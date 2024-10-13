# cook your dish here
t=int(input())

for i in range(t):
    n , k=map(int,(input()).split())
    l=list(map(int,(input()).split()))
    f,g=[],[]
    for j in range(n):
        if j%2==0:
            f.append(l[j])
        else:
            g.append(l[j])
    z=0
    while(z<k):
        a=max(f)
        b=min(g)
        f.remove(a)
        g.append(a)
        g.remove(b)
        f.append(b)
        z=z+1
     
    if sum(f) < sum(g):
        print("YES")
    else:
        print("NO")
    
