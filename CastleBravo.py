print("\n*********************************\n")

print("Weather Branch\n")

#import libraries here
import random
from time import sleep

def weather():
    weatherForcast = ["snowing", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

print(weather())