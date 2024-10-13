# cook your dish here


t=int(input())
for z in range(t):
    size=int(input())
    nums=list(map(int, input().split()))
    for j in range(size):
        nums[j]=abs(nums[j])
    add=sorted(nums[0:size:2])
    sub=sorted(nums[1:size:2],reverse=True)
    if(add[0]<sub[0]):
        add[0],sub[0]=sub[0],add[0]
    print(sum(add)-sum(sub))    
