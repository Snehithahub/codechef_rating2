def solve():
    n = int(input())  # Length of the binary string
    binary_string = input()  # The binary string (either '1's and '0's)
    
    count_1 = 0  # To count the number of '1's in the string
    for char in binary_string:
        if char == '1':
            count_1 += 1  # Increment count_1 if we encounter '1'
    
    count_0 = n - count_1  # Count of '0's is total length minus '1's
    
    # The answer is based on the minimum of count_1 and count_0
    answer = min(count_1, count_0)
    
    # If the minimum count is even, print "Ramos", otherwise print "Zlatan"
    if answer % 2 == 0:
        print("Ramos")
    else:
        print("Zlatan")

# Number of test cases
t = int(input())
for _ in range(t):
    solve()
