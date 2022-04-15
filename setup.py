import pigpio

RED = 18  # The red LED is on GPIO pin 18
YEL = 23  # The yellow LED is on GPIO pin 23
GRE = 24  # The green LED is on GPIO pin 24

colours = [GRE, YEL, RED]  # All the LEDs in the order we want to work with them.


# This function will configure a list of pins to be GPIO output pins
def configure_output_pins(gpio, pins):
    for pin in pins:
        gpio.set_mode(pin, pigpio.OUTPUT)
        gpio.set_pull_up_down(pin, pigpio.PUD_OFF)
        gpio.write(pin, 0)


# Set all pins in the list to off. Useful before exiting.
def set_all_pins_off(gpio, pins):
    for pin in pins:
        gpio.write(pin, 0)
