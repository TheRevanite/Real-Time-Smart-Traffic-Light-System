from gpiozero import AngularServo
from time import sleep

signalPIN = 14 #DEFINING THE GPIO PIN TO WHICH MOTOR IS CONNECTED
servo = AngularServo(signalPIN, min_angle=0, max_angle=360, min_pulse_width=0.0005, max_pulse_width=0.0024)

def roads1(duration):
  servo.angle = 90 #or 45
  sleep(duration-1)

def roads2(duration):
  servo.angle = 270 # or 225
  sleep(duration-1)
