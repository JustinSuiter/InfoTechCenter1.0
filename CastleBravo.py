import sys
import time

# Define ANSI escape codes for various colors and reset
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Display a welcome message when the program starts (using the selected color)
print(CYAN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

timeToSleep = 1.5 #variable to set the time library to 1.5 seconds when called
time.sleep(timeToSleep) # Calling the timeToSleep library with the variable timeToSleeps value

# Initialize variables for loop control
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Counter for adding dots after the booting message

# Loop that runs 20 times to simulate a system booting process
while x != 20:
    x += 1  # Increment the counter on each iteration

    # Construct a message that changes by adding one more dot (in the selected color)
    message = BLUE + "InfoTechCenter System Booting" + "." * ellipsis + RESET

    # Increment the number of dots after the message
    ellipsis += 1

    # Use sys.stdout.write to update the message in-place (without creating a new line)
    sys.stdout.write("\r" + message)

    # Pause for half a second before the next iteration, to simulate the system taking time to boot
    time.sleep(.5)

    # Reset the ellipsis counter to 0 after reaching 3 dots (for a repeating sequence of 0-3 dots)
    if ellipsis == 4:
        ellipsis = 0

    # When the loop finishes after 20 iterations, display a final boot-up message (in the selected color)
    if x == 20:
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted" + RESET)

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
