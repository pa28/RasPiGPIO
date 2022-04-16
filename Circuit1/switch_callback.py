#!/usr/bin/env python3
import time

import pigpio  # Pi GPIO library
import LED_SX

SLEEP = 0.2  # Length of time to sleep

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)


# Keyboard interrupt handler to exit the program gracefully
def keyboard_interrupt_handler(sig, frame):
    print("Keyboard interrupt (ID: {}), cleaning up.".format(sig))
    LED_SX.clean_up_exit(pi, 0)


# Switch callback function
def switch_callback(gpio, level, tick):
    print("Switch callback (Pin: {}, Level: {}, Tick: {}.".format(gpio, level, tick))


LED_SX.set_keyboard_interrupt(keyboard_interrupt_handler)

# Configure the pins for output.
LED_SX.configure_pins(pi)

pi.callback(pigpio.EITHER_EDGE, switch_callback)
while True:
    for led in LED_SX.colours:  # For each colour LED
        LED_SX.set_led_state(pi, led, 1)  # Turn the LED on
        time.sleep(SLEEP)  # Wait for SLEEP seconds
        LED_SX.set_led_state(pi, led, 0)  # Turn the LED off

