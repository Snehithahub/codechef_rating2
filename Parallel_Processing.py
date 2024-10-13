for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(A[0])
    else:
        total_sum = sum(A)
        prefix_sum = 0
        min_time = float('inf')

        for i in range(N - 1):
            prefix_sum += A[i]
            # Time taken is the maximum of the two processor times
            max_time = max(prefix_sum, total_sum - prefix_sum)
            min_time = min(min_time, max_time)

        print(min_time)
