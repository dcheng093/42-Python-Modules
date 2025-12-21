#!/usr/bin/python3.10

def check_temperature(temp_str):
    try:
        num = int(temp_str)
        if num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)")
        elif num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {num}°C is perfect for plants!")
        return num
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")

def test_temperature_input():
    