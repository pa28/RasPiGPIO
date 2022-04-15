#!/usr/bin/env python3

import time     # Needed for sleep function
import pigpio   # Pi GPIO library
import setup    # Our set-up.

SLEEP = 0.2     # Length of time to sleep
REPS = 20       # Number of times to repeat.

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)

# Configure the pins for output.
setup.configure_output_pins(pi, setup.colours)

# Loop for the number of repetitions.
for t in range(REPS):
    for on in setup.colours:    # For each colour LED
        pi.write(on, 1)         # Turn the LED on
        time.sleep(SLEEP)       # Wait for SLEEP seconds
        pi.write(on, 0)         # Turn the LED off

# Finish up by turning all the LEDs off.
setup.set_all_pins_off(pi, setup.colours)

# Disconnect from the Raspberry Pi
pi.stop()
