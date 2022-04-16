#!/usr/bin/env python3
import time

import pigpio  # Pi GPIO library
import LED_SX

SLEEP = 1  # Length of time to sleep
run = True

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)


# Keyboard interrupt handler to exit the program gracefully
def keyboard_interrupt_handler(sig, frame):
    print("Keyboard interrupt (ID: {}), cleaning up.".format(sig))
    pi.event_trigger(0)


# Switch callback function
def switch_callback(gpio, level, tick):
    print("Switch callback (Pin: {}, Level: {}, Time: {}).".format(gpio, level, tick))
    if level:
        pi.event_trigger(0)


LED_SX.set_keyboard_interrupt(keyboard_interrupt_handler)

# Configure the pins for output.
LED_SX.configure_pins(pi)

pi.set_glitch_filter(LED_SX.PUSH_BUTTON, 1000)
pi.callback(LED_SX.PUSH_BUTTON, pigpio.RISING_EDGE, switch_callback)

while run:
    for led in LED_SX.colours:  # For each colour LED
        LED_SX.set_led_state(pi, led, 1)  # Turn the LED on
        if pi.wait_for_event(0, SLEEP):
            run = False
            break
        LED_SX.set_led_state(pi, led, 0)  # Turn the LED off

LED_SX.clean_up_exit(pi, 0)
