for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = []
    
    for i in range(n):
        for j in range(i + 1, n):
            d.append(abs(a[i] + a[j] - k))
    
    min_diff = min(d)
    print(min_diff, d.count(min_diff))
