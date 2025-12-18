def ft_count_harvest_recursive(n=None, days=1):
    if n is None:
        n = int(input("Days until harvest: "))
    if days > n:
        print("Harvest time!")
        return
    print(f"Day {days}")
    ft_count_harvest_recursive(n, days + 1)
