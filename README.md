# Simon Says
A simple Simon Says game utilizing Raspberry Pi GPIO ports. This repository contains the schematic for the circuit and a Python script to be run on the Raspberry Pi.

## Required Python Libraries
* digitalio
* RPi.GPIO (or RPi)
* adafruit_character_lcd

## Circuit Components
* 1 Raspberry Pi 4 Model B
* 1 Breadboard
* 1 RGB LED (common cathode)
* 1 LCD display (16x2)
* 1 10kΩ potentiometer
* 1 Buzzer
* 5 220Ω resistors
* 3 Push buttons (one for each color: red, green, blue)
* Jumper wires

## How to Play
Run the Python script after building the circuit. The RGB LED will display a sequence of colors (red, green, and blue) separated by white. The goal of the game is to repeat the exact same sequence using the buttons. 
For each correct sequence, the player will be awarded points (displayed on the LCD). Each time the player makes a mistake, the buzzer will play. After 3 mistakes, the game ends.
