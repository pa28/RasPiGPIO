#!/usr/bin/env python3

import pigpio  # Pi GPIO library
import LED_SX  # Our set-up.

SLEEP = 0.03  # Length of time to sleep
REPS = 10  # Number of times to repeat.

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)


# Keyboard interrupt handler to exit the program gracefully
def keyboard_interrupt_handler(sig, frame):
    print("Keyboard interrupt (ID: {}), cleaning up.".format(sig))
    LED_SX.clean_up_exit(pi, 0)


LED_SX.set_keyboard_interrupt(keyboard_interrupt_handler)

# Configure the pins for output.
LED_SX.configure_pins(pi)

# Loop for the number of repetitions.
while True:
    for led in LED_SX.colours:  # For each colour LED
        LED_SX.set_led_state(pi, led, 1)  # Turn the LED on
        LED_SX.sleep_exit_on_button(pi, 0.5)  # Wait for SLEEP seconds
        LED_SX.set_led_state(pi, led, 0)  # Turn the LED off
        LED_SX.sleep_exit_on_button(pi, 0.5)  # Wait for SLEEP seconds
