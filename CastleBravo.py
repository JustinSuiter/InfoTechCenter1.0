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
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 55mph")
    elif weatherAlert == "blizzard":
        print("\nThe Nation Weather Service has updated our alarm by 45 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 45mph")
    elif weatherAlert == "rainy":
        print("\nThe Nation Weather Service has updated our alarm by 15 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 65mph")
    elif weatherAlert == "windy":
        print("\nThe Nation Weather Service has updated our alarm by 5 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nThe Nation Weather Service has updated our alarm by 50 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 35mph")
    else:
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS System has been disengaged")
vehicleResponseSystem()