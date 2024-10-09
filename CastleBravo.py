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

# You can change the color below to any defined color (e.g., RED, GREEN, BLUE, etc.)
welcome_color = CYAN
selected_color = BLUE  # Change this to any color you prefer
exit_color = GREEN


# Display a welcome message when the program starts (using the selected color)
print(welcome_color + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

# Initialize variables for loop control
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Counter for adding dots after the booting message

# Loop that runs 20 times to simulate a system booting process
while x != 20:
    x += 1  # Increment the counter on each iteration

    # Construct a message that changes by adding one more dot (in the selected color)
    message = selected_color + "InfoTechCenter System Booting" + "." * ellipsis + RESET

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
        print(exit_color + "\n\nOperating System Booted Up - Retina Scanned - Access Granted" + RESET)