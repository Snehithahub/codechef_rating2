for _ in range(int(input())):
    n, x, y = map(int, input().split())
    
    cars_needed = (n + 3) // 4
    smoke_using_cars = cars_needed * y
    
    buses_needed = n // 100
    remaining_people = n % 100
    smoke_using_buses = buses_needed * x

    if remaining_people > 0:
        smoke_using_buses += x
        cars_needed_remaining = (remaining_people + 3) // 4
        smoke_using_buses = min(smoke_using_buses, (buses_needed * x) + (cars_needed_remaining * y))
    
    print(min(smoke_using_cars, smoke_using_buses))
