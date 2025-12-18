def ft_water_reminder():
    reminder = int(input("Days since last watering: "))
    print("Water the plants!" if reminder > 2 else "Plants are fine")
