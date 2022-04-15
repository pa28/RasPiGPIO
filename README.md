# RasPiGPIO
This repo has the Fitzing diagrams and Python software for some Raspberry Pi GPIO programming examples I have put together for a youth
introduction to programming course.

## Circuit 1

![LEDs and Switch](https://github.com/pa28/RasPiGPIO/blob/main/FritzingSketches/LED%20SX%20Wiring_bb.png)

## [Setup File](https://github.com/pa28/RasPiGPIO/blob/main/Circuit1/LED_SX.py)

This file contains constants and helper functions to make is easier to program actions of the circuit and help maintain readability of those programs.

## [Setup Test](https://github.com/pa28/RasPiGPIO/blob/main/Circuit1/LED_SX_TEST.py)

A quick test program to ensure the circuit has been set up and is working properly with the setup file.

## [sequence.py](https://github.com/pa28/RasPiGPIO/blob/main/Circuit1/sequence.py)

Illuminate one LED at a time, in squence, until the push button is pressed.

## [flashing_lights.py](https://github.com/pa28/RasPiGPIO/blob/main/Circuit1/flashing_lights.py)

Turn each LED on then off, in sequecne, until the push button is pressed.

## [random_lights.py](https://github.com/pa28/RasPiGPIO/blob/main/Circuit1/random_lights.py)

Turn LEDs on and off at random until the push button is pressed.
