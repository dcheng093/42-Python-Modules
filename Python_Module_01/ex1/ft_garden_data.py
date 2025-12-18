#!/usr/bin/env python3.10

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    garden = [plant1, plant2, plant3]
    print("=== Garden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
