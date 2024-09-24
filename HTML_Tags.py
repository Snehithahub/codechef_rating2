# cook your dish here
for _ in range(int(input())):
    S=input().strip()
    if (S[0]=="<" and S[1]=="/" and S[-1]==">" and len(S[2:-1])>0):
        S = S[2:-1]
        if S.isnumeric():
            print("Success")
        elif S.isalnum() and S.islower():
            print("Success")
        else:
            print("Error")
    else:
        print("Error")
      
