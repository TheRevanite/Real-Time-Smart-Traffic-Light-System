from gpiozero import LED
from time import sleep

def setup():
    PIN_MAPPING = {
        'red': [2, 17, 0, 16],
        'yellow': [3, 27, 5, 20],
        'green': [4, 22, 6, 21]
    }
    global leds
    leds = {color: [LED(pin) for pin in pins] for color, pins in PIN_MAPPING.items()}
    
    for led in leds['red']:
        led.on()

    print("Setup complete")
    return leds

def light_on(index):
    # Assuming index is 1-based and maps to a 1-based group of LEDs
    group = [leds['red'][index-1], leds['yellow'][index-1], leds['green'][index-1]]
    group[0].off()    # Turn off red light
    group[1].on()     # Turn on yellow light
    sleep(1)
    group[1].off()    # Turn off yellow light
    group[2].on()     # Turn on green light   

def wait(duration):
    sleep(duration)

def light_off(index):
    # Assuming index is 1-based and maps to a 1-based group of LEDs
    group = [leds['red'][index-1], leds['yellow'][index-1], leds['green'][index-1]]
    group[2].off()    # Turn off green light
    group[1].on()     # Turn on yellow light
    sleep(2)
    group[1].off()    # Turn off yellow light
    group[0].on()     # Turn on red light