#!/usr/bin/env python3

import pigpio
import LED_SX
import time

SLEEP = 0.5     # Length of time to sleep

# Connect to a Raspberry Pi on port 8888
pi = pigpio.pi("devw.local", 8888)
if not pi.connected:
    exit(1)

# Configure the pins for output.
LED_SX.configure_pins(pi)

while True:
    for led in LED_SX.colours:
        if led == LED_SX.RED:
            print("RED")
        elif led == LED_SX.GRE:
            print("GREEN")
        elif led == LED_SX.YEL:
            print("YELLOW")
        else:
            print("Bad LED pin.")
        LED_SX.set_led_state(pi, led, 1)
        if LED_SX.read_push_button(pi):
            print("Button pushed.")
        time.sleep(SLEEP)
        LED_SX.set_led_state(pi, led, 0)
    print("")

