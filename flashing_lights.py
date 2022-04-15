
import time     # Needed for sleep function
import pigpio   # Pi GPIO library
import setup    # Our set-up.

SLEEP = 0.03    # Length of time to sleep
REPS = 10       # Number of times to repeat.

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)

setup.configure_output_pins(pi, setup.colours)

# Loop for the number of repetitions.
for t in range(REPS):
    for led in setup.colours:   # For each colour LED
        pi.write(led, 1)        # Turn the LED on
        time.sleep(0.5)         # Wait for SLEEP seconds
        pi.write(led, 0)        # Turn the LED off
        time.sleep(0.5)         # Wait for SLEEP seconds

# Finish up by turning all the LEDs off.
setup.set_all_pins_off(pi, setup.colours)

# Disconnect from the Raspberry Pi
pi.stop()
