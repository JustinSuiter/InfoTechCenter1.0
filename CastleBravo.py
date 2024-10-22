# Print a formatted separator for better readability in the console output
print("\n**********************************************\n")

# Print the title of the program to indicate which branch is running
print("Gasoline Branch\n")

# Import the random module to enable random selection from lists later in the code
# Import the sleep function from time module to simulate delays in program execution
import random
from time import sleep


# Function to simulate the current gas level
def gasLevelGauge():
    # List of possible gas levels, ranging from "Empty" to "Full"
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select and return one of the gas levels from the list
    return random.choice(gasLevelList)


# Function to simulate a random nearby gas station
def gasStations():
    # List of possible gas stations
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly select and return one of the gas stations from the list
    return random.choice(gasStationsList)


# Function to determine the gas level and provide appropriate alerts
def gasLevelAlert():
    # Randomly generate a distance to the nearest gas station if the gas level is "Low"
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Randomly generate a distance to the nearest gas station if the gas level is "Quarter Tank"
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level using the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and provide appropriate messages based on the result
    if gasLevelIndicator == "Empty":
        # If the gas tank is empty, provide a warning and simulate calling for help
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(1.5)  # Pause for 1.5 seconds to simulate processing time
        print("Calling Triple AAA")  # Simulate an action of calling roadside assistance
    elif gasLevelIndicator == "Low":
        # If the gas tank is low, advise the user to find a nearby gas station
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(1.5)  # Pause for realism
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        # If the gas tank is at a quarter tank, provide a similar alert for a nearby gas station
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(1.5)  # Pause for realism
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        # If the gas tank is half full, reassure the user that they have enough fuel
        print('Your gas tank is a half a tank full, which is plenty to get to your destination')
    elif gasLevelIndicator == "Three Quarter Tank":
        # If the gas tank is three quarters full, reassure the user they have plenty of fuel
        print('Your gas tank is a three quarters of the way full, which is plenty to get to your destination')
    else:
        # If the gas tank is full, the user is ready to go without concern
        print("Your gas tank is full!! Vroom Vroom")


# Call the gasLevelAlert function to start the program
gasLevelAlert()