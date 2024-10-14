# cook your dish here
for _ in range(int(input())):
    n,h,y1,y2,l=map(int,input().split())
    count=0
    for i in range(n):
        t,x=map(int,input().split())
        if(t==2):
            
                if(y2>=x):
                    pass    
                else:    
                    l=l-1
                    
        else:
            if(h-y1>x):
                l=l-1
        if l>=1:
            count=count+1
    print(count)
