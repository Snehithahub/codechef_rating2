t = int(input())
for _ in range(t):
    D, d, P, Q = map(int, input().split())
    
    complete_periods = D // d
    remaining_days = D % d
    
    # Sum earnings for complete periods using arithmetic progression sum formula
    total_amount = d * complete_periods * P + d * Q * (complete_periods * (complete_periods - 1)) // 2
    
    # Sum earnings for remaining days
    total_amount += remaining_days * (P + complete_periods * Q)

    print(total_amount)
