
import time     # Needed for sleep function
import random   # Generate random numbers
import pigpio   # Pi GPIO library
import setup    # Our set-up.

SLEEP = 0.15    # Length of time to sleep
REPS = 100      # Number of times to repeat.

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)

setup.configure_output_pins(pi, setup.colours)
random.seed()   # Initialize Random number generator

# Loop for the number of repetitions.
while REPS:
    for led in setup.colours:       # For each colour LED
        r = random.randint(0, 1)    # Turn the LED on or off randomly
        pi.write(led, r)
    time.sleep(SLEEP)               # Wait for SLEEP seconds.

# Finish up by turning all the LEDs off.
setup.set_all_pins_off(pi, setup.colours)

# Disconnect from the Raspberry Pi
pi.stop()
