# cook your dish here
def main():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the length of the string
        s = input()  # Read the string itself
        cnt = 0
        
        # Count the number of changes between adjacent characters
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                cnt += 1
        
        # Output the result based on the count
        if cnt % 2 == 0:
            print(cnt // 2)
        else:
            print((cnt + 1) // 2)

if __name__ == "__main__":
    main()
