print("\n*********************************\n")

print("Weather Branch\n")

#import libraries here
import random
from time import sleep

def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe Nation Weather Service has updated our alarm by 30 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")

vehicleResponseSystem()