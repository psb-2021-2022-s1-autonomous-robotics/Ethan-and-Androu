# Add your Python code here. E.g.
from microbit import *

def turn(pin, angle, cw, period=10):
    """Turn servo on pin to angle"""
    
    pin.write_analog(percent * 1023)
    
pin15.set_analog_period(10)
pin16.set_analog_period(10)
while True:
    turn(pin15, 90, True)
    turn(pin16, 90, True)
    
    