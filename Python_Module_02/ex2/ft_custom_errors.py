#!/usr/bin/python3.10

class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__("Caught a garden error: " + message)


class PlantError(GardenError):
    def __init__(self, plant: str, message: str):
        super().__init__("Caught PlantError: " + message)


class WaterError(GardenError):
    def __init__(self, water: str, message: str):
        super().__init__("Caught WaterError: " + message)


def plant_error()