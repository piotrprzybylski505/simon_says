import RPi.GPIO as GPIO
import time
import random
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

#LCD SETUP
lcd_rs = digitalio.DigitalInOut(board.D24)
lcd_en = digitalio.DigitalInOut(board.D25)
lcd_d7 = digitalio.DigitalInOut(board.D21)
lcd_d6 = digitalio.DigitalInOut(board.D20)
lcd_d5 = digitalio.DigitalInOut(board.D26)
lcd_d4 = digitalio.DigitalInOut(board.D16)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

#INPUT\OUTPUT SETUP
pin_red = 17 #11
pin_green = 27 #13
pin_blue = 22 #15
pin_buzz = 9 #21
in_red = 5 #29
in_green = 6 #31
in_blue = 13 #33

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red,GPIO.OUT)
GPIO.setup(pin_green,GPIO.OUT)
GPIO.setup(pin_blue,GPIO.OUT)
GPIO.setup(pin_buzz, GPIO.OUT)
GPIO.setup(in_red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in_green, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in_blue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def turn_off():
    GPIO.output(pin_red, GPIO.HIGH)
    GPIO.output(pin_green, GPIO.HIGH)
    GPIO.output(pin_blue, GPIO.HIGH)

def white():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_green, GPIO.LOW)
    GPIO.output(pin_blue, GPIO.LOW)

def red():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_green, GPIO.HIGH)
    GPIO.output(pin_blue, GPIO.HIGH)

def green():
    GPIO.output(pin_red, GPIO.HIGH)
    GPIO.output(pin_green, GPIO.LOW)
    GPIO.output(pin_blue, GPIO.HIGH)

def blue():
    GPIO.output(pin_red, GPIO.HIGH)
    GPIO.output(pin_green, GPIO.HIGH)
    GPIO.output(pin_blue, GPIO.LOW)

def buzz():
    GPIO.output(pin_buzz, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin_buzz, GPIO.LOW)
    
def in_color():
    while True:
        if GPIO.input(in_red)==GPIO.HIGH:
            return "red"
        if GPIO.input(in_green)==GPIO.HIGH:
            return "green"
        if GPIO.input(in_blue)==GPIO.HIGH:
            return "blue"

def display_color(color, delay=1):
    if color=="red":
        red()
    elif color=="green":
        green()
    elif color=="blue":
        blue()
    time.sleep(delay)
    turn_off()

def display_sequence(sequence, delay=1, interval=1):
    white()
    time.sleep(1)
    turn_off()
    time.sleep(interval)
    for clr in sequence:
        display_color(clr, delay)
        time.sleep(interval)
    white()
    time.sleep(1)
    turn_off()

def check_sequence(sequence):
    for clr in sequence:
        color_choice = in_color()
        if (color_choice==clr):
            display_color(clr)
        else:
            buzz()
            return True
    white()
    time.sleep(1)
    turn_off()

def generate_sequence(length):
    seq = []
    for i in range(length):
        seq.append(random.choice(["red", "green", "blue"]))
    return seq

color_choice = "NULL"
score = 0
turn_off()
test_seq = ["red", "green", "blue"]
seq_length = 3
light_duration = 1
light_interval = 1
lives = 3

lcd.clear()
lcd.message = "Starting Game"
display_sequence(test_seq, 0.25, 0)
lcd.clear()

lcd.message = "Score:" + str(score) + "\nLives:" + lives*"O"
while True:
    time.sleep(2)
    sequence = generate_sequence(seq_length)
    display_sequence(sequence, light_duration, light_interval)
    if (check_sequence(sequence)):
        lives-=1
        if lives<=0:
            lcd.clear()
            lcd.message = "GAME OVER\nScore:" + str(score)
            time.sleep(3)
            break
        else:
            lcd.clear()
            lcd.message = "Score:" + str(score) + "\nLives:" + lives*"O"
    else:
        score+=100
        lcd.clear()
        lcd.message = "Score:" + str(score) + "\nLives:" + lives*"O"
        seq_length+=1
        light_duration = light_duration*0.9
        light_interval = light_interval*0.8

lcd.clear()        
GPIO.cleanup()

