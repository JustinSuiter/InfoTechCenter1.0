print("\n*********************************\n")
print("Weather Branch\n")

# Import necessary libraries
import random
from time import sleep


def weather():
    """
    This function selects a random weather condition from a predefined list.
    Returns:
        A randomly chosen weather condition.
    """
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    return random.choice(weatherForcast)


# Dictionary to store alarm delay and speed limit for each weather condition
weather_conditions = {
    "snowy": {"delay": 30, "speed": 55},
    "blizzard": {"delay": 45, "speed": 45},
    "rainy": {"delay": 15, "speed": 65},
    "windy": {"delay": 5, "speed": 70},
    "icy": {"delay": 50, "speed": 35},
    "sunny": {"delay": 0, "speed": None},  # For sunny, no delay and no speed limit enforced
}

weatherAlert = weather()


def vehicleResponseSystem():
    """
    Adjusts vehicle response based on the weather condition,
    such as updating alarm time and setting a speed limit.
    """
    if weatherAlert in weather_conditions:
        # Get the delay and speed for the current weather condition
        delay = weather_conditions[weatherAlert]["delay"]
        speed = weather_conditions[weatherAlert]["speed"]

        # Print the delay message
        print(f"\nThe Nation Weather Service has updated our alarm by {delay} minutes because "
              f"of the forecast of {weatherAlert} weather conditions.")
        sleep(1)  # Pause for 1 second

        # Print the speed limit message if there's a speed restriction
        if speed is not None:
            print(f"\nVRS System has been engaged only allowing you to drive {speed}mph")
        else:
            print("\nVRS System has been disengaged, drive carefully!")
    else:
        # If the weather is not in the dictionary (just in case)
        print(f"\nThe NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS System has been disengaged")


vehicleResponseSystem()