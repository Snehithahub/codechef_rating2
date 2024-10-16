for _ in range(int(input())):
    l, r = map(int, input().split())
    count = 0

    for num in range(l, r + 1):  # Include r in the range
        digit_sum = 0
        x = num
        while x != 0:
            digit_sum += x % 10  # Sum the digits
            x //= 10
            
        # Check if the sum of digits is divisible by 3
        if digit_sum % 3 == 0:
            count += 1
            
    print(count)
