#!/usr/bin/env python3.10

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        self.height += cm

    def age_by(self, days):
        self.age += days

    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    garden = [plant1, plant2, plant3]

    print("=== Day 1 ===")
    for plant in garden:
        print(plant.get_info())
    days = 6
    growth_per_plant = {"Rose": 6, "Sunflower": 200, "Cactus": 2}
    for plant in garden:
        plant.age_by(days)
        plant.grow(growth_per_plant[plant.name])

    print("\n=== Day 7 ===")
    for plant in garden:
        print(plant.get_info())
        print(f"Growth this week: +{growth_per_plant[plant.name]}cm")
