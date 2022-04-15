#!/usr/bin/env python3

import pigpio   # Pi GPIO library
from Circuit1 import LED_SX

SLEEP = 0.2     # Length of time to sleep

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)

# Configure the pins for output.
LED_SX.configure_pins(pi)

# Loop for the number of repetitions.
while True:
    for led in LED_SX.colours:                    # For each colour LED
        LED_SX.set_led_state(pi, led, 1)          # Turn the LED on
        LED_SX.sleep_exit_on_button(pi, SLEEP)    # Wait for SLEEP seconds
        LED_SX.set_led_state(pi, led, 0)          # Turn the LED off

# Finish up by turning all the LEDs off and exiting.
LED_SX.clean_up_exit(pi, 0)
