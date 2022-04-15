import pigpio
import time

RED = 18  # The red LED is on GPIO pin 18
YEL = 23  # The yellow LED is on GPIO pin 23
GRE = 24  # The green LED is on GPIO pin 24

PUSH_BUTTON = 17    # The push button is on GPIO pin 17

colours = [GRE, YEL, RED]  # All the LEDs in the order we want to work with them.


# This function will configure a list of pins to be GPIO output pins
def configure_pins(gpio):
    for pin in colours:
        gpio.set_mode(pin, pigpio.OUTPUT)
        gpio.set_pull_up_down(pin, pigpio.PUD_OFF)
        gpio.write(pin, 0)
    # Configure push button switch
    gpio.set_pull_up_down(PUSH_BUTTON, pigpio.PUD_OFF)
    gpio.set_mode(PUSH_BUTTON, pigpio.INPUT)


# Set all pins in the list to off. Useful before exiting.
def set_all_leds_off(gpio):
    for pin in colours:
        gpio.write(pin, 0)


# Turn a particular LED on or off
def set_led_state(gpio, led, state):
    if led in colours:
        gpio.write(led, state)


# Cleanup and exit
def clean_up_exit(gpio, exit_code):
    set_all_leds_off(gpio)
    gpio.stop()
    exit(exit_code)


# Read the button
def read_push_button(gpio):
    return gpio.read(PUSH_BUTTON)


# Sleep but exit on push button press
def sleep_exit_on_button(gpio, seconds):
    if gpio.read(PUSH_BUTTON):
        clean_up_exit(gpio, 0)
    time.sleep(seconds)
    if gpio.read(PUSH_BUTTON):
        clean_up_exit(gpio, 0)
