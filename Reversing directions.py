for _ in range(int(input())):
    a = []
    d = []
    inputs = int(input())
    
    for l in range(inputs):
        x = input().split()
        a.append(x[0])  # Store the first word (Begin/Left/Right)
        d.append(" ".join(x[2:]))  # Store the road name

    # Reverse the lists
    a.reverse()
    d.reverse()

    # Swap directions
    for s in range(len(a)):
        if a[s] == 'Left':
            a[s] = "Right"
        elif a[s] == 'Right':
            a[s] = "Left"
    # Correctly print the reversed directions
    gg=a[len(a)-1]
    k=[gg]
    for f in range(0,len(a)-1):
        k.append(a[f])
    
    c=[]
    for g in range(0,len(a)):
        c.append(k[g]+" on "+d[g])
    for h in range(0,inputs):
        print(c[h])

    print("")  # Blank line after each test case
"""
i/p:
2
4
Begin on Road A
Right on Road B
Right on Road C
Left on Road D
6
Begin on Old Madras Road
Left on Domlur Flyover
Left on 100 Feet Road
Right on Sarjapur Road
Right on Hosur Road
Right on Ganapathi Temple Road
o/p:
Begin on Road D
Right on Road C
Left on Road B
Left on Road A

Begin on Ganapathi Temple Road
Left on Hosur Road
Left on Sarjapur Road
Left on 100 Feet Road
Right on Domlur Flyover
Right on Old Madras Road
"""
