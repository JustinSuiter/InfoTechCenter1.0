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

print("\n**********************************************\n")
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

import random
from time import sleep

# Print a formatted separator for better readability in the console output
print("\n**********************************************\n")

# Print the title of the program to indicate which branch is running
print("Gasoline Branch\n")


# Function to simulate the current gas level
def gasLevelGauge():
    # List of possible gas levels, ranging from "Empty" to "Full"
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)


# Function to simulate a random nearby gas station
def gasStations():
    # List of possible gas stations
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)


# Function to provide alerts based on gas level
def gasLevelAlert():
    # Randomly generate distances to the nearest gas station
    gasStationDistances = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Get the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Define responses for each gas level
    gasResponses = {
        "Empty": ("***WARNING - YOU ARE ON EMPTY***\n", "Calling Triple AAA"),
        "Low": ("Your gas tank is extremely low, checking GPS for the closest gas station",
                f"The closest gas station is {gasStations()} which is {gasStationDistances['Low']} miles away."),
        "Quarter Tank": ("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station",
                         f"The closest gas station is {gasStations()} which is {gasStationDistances['Quarter Tank']} miles away."),
        "Half Tank": ("Your gas tank is half full, you have plenty of fuel to reach your destination",),
        "Three Quarter Tank": ("Your gas tank is three-quarters full, enough fuel to reach your destination",),
        "Full Tank": ("Your gas tank is full!! Vroom Vroom",)
    }

    # Retrieve the appropriate response based on gas level
    response = gasResponses.get(gasLevelIndicator)

    # Print the messages, with a pause if needed
    print(response[0])
    sleep(1.5)  # Simulate processing delay
    if len(response) > 1:  # If there are additional messages, print them
        print(response[1])


# Run the gas level alert program
gasLevelAlert()
