import sys
import time

# Display a welcome message when the program starts
print("\nWelcome to InfoTechCenter V1.0\n")

# Initialize variables for loop control
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Counter for adding dots after the booting message

# Loop that runs 20 times to simulate a system booting process
while x != 20:
    x += 1  # Increment the counter on each iteration

    # Construct a message that changes by adding one more dot (.)
    message = ("InfoTechCenter System Booting" + "." * ellipsis)

    # Increment the number of dots after the message
    ellipsis += 1

    # Use sys.stdout.write to update the message in-place (without creating a new line)
    sys.stdout.write("\r" + message)

    # Pause for half a second before the next iteration, to simulate the system taking time to boot
    time.sleep(.5)

    # Reset the ellipsis counter to 0 after reaching 3 dots (for a repeating sequence of 0-3 dots)
    if ellipsis == 4:
        ellipsis = 0

    # When the loop finishes after 20 iterations, display a final boot-up message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")