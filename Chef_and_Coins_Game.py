# Cook your dish here
for _ in range(int(input())):
    x = int(input())
    flag = 0 

    if x == 1:
        flag = 1
    elif x <= 3:
        flag = 0     
    elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        flag = 1
       
    for i in range(5, int(x**0.5) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            flag = 1

    if flag == 0:
        print("misha")
    else:
        print("chef")
