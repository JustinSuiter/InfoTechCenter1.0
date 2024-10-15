print("\n*********************************\n")  # Prints a decorative line of asterisks to separate output
print("Weather Branch\n")  # Prints a label for the section of code

# Import libraries here
import random  # Imports the 'random' module to use for selecting a random weather condition
from time import sleep  # Imports the 'sleep' function to pause the program for a specified amount of time

def weather():
    """
    This function selects a random weather condition from a predefined list.
    Returns:
        A randomly chosen weather condition.
    """
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]  # List of possible weather conditions
    weatherCondition = random.choice(weatherForcast)  # Randomly selects one condition from the list
    return weatherCondition  # Returns the selected weather condition

weatherAlert = weather()  # Calls the 'weather' function and stores the result in 'weatherAlert'

def vehicleResponseSystem():
    """
    Based on the weather condition, this function determines the appropriate vehicle response,
    like adjusting alarm time and setting a speed limit.
    """
    if weatherAlert == "snowy":  # If the weather is snowy
        print("\nThe Nation Weather Service has updated our alarm by 30 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")  # Inform user of 30-minute delay
        sleep(1)  # Pauses for 1 second
        print("\nVRS System has been engaged only allowing you to drive 55mph")  # Restricts speed to 55mph

    elif weatherAlert == "blizzard":  # If the weather is a blizzard
        print("\nThe Nation Weather Service has updated our alarm by 45 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")  # Inform user of 45-minute delay
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 45mph")  # Restricts speed to 45mph

    elif weatherAlert == "rainy":  # If the weather is rainy
        print("\nThe Nation Weather Service has updated our alarm by 15 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")  # Inform user of 15-minute delay
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 65mph")  # Restricts speed to 65mph

    elif weatherAlert == "windy":  # If the weather is windy
        print("\nThe Nation Weather Service has updated our alarm by 5 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")  # Inform user of 5-minute delay
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 70mph")  # Restricts speed to 70mph

    elif weatherAlert == "icy":  # If the weather is icy
        print("\nThe Nation Weather Service has updated our alarm by 50 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.")  # Inform user of 50-minute delay
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 35mph")  # Restricts speed to 35mph

    else:  # If the weather is sunny or any other condition not explicitly handled
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")  # Inform user to drive carefully
        sleep(1)
        print("\nVRS System has been disengaged")  # No speed limit imposed

vehicleResponseSystem()  # Calls the function to execute the appropriate vehicle response based on weather