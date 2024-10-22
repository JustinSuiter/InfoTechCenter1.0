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