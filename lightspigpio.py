from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

def setup():
    PIN_MAPPING = {
        'red': [2, 17, 0, 16],
        'yellow': [3, 27, 5, 20],
        'green': [4, 22, 6, 21]
    }
    global leds
    factory = PiGPIOFactory()  # Use pigpio as the backend for gpiozero
    
    # Initialize LEDs with gpiozero and pigpio
    leds = {
        'red': [LED(pin, pin_factory=factory) for pin in PIN_MAPPING['red']],
        'yellow': [LED(pin, pin_factory=factory) for pin in PIN_MAPPING['yellow']],
        'green': [LED(pin, pin_factory=factory) for pin in PIN_MAPPING['green']],
    }
    
    # Set all red LEDs to ON initially
    for led in leds['red']:
        led.on()

    print("Setup complete")
    return leds

def light_on(index):
    # Assuming index is 1-based and maps to a 1-based group of LEDs
    leds['red'][index-1].off()  # Turn off red light
    leds['yellow'][index-1].on()  # Turn on yellow light
    sleep(1)
    leds['yellow'][index-1].off()  # Turn off yellow light
    leds['green'][index-1].on()  # Turn on green light   

def wait(duration):
    sleep(duration)

def light_off(index):
    # Assuming index is 1-based and maps to a 1-based group of LEDs
    leds['green'][index-1].off()  # Turn off green light
    leds['yellow'][index-1].on()  # Turn on yellow light
    sleep(2)
    leds['yellow'][index-1].off()  # Turn off yellow light
    leds['red'][index-1].on()  # Turn on red light

# Don't forget to clean up when you're done
def cleanup():
    for led_list in leds.values():
        for led in led_list:
            led.close()
