import machine
import utime
led_onboard = machine.Pin(15, machine.Pin.OUT)

def dah():
    light(.25)
    
def dash():
    light(.5)
    
def light(delay):
    led_onboard.value(1)
    utime.sleep(delay)
    led_onboard.value(0)
    utime.sleep(delay)
    
    
while True:
    dah()
    dah()
    dah()
    utime.sleep(1)
    dash()
    dash()
    dash()
    utime.sleep(1)
    dah()
    dah()
    dah()
    utime.sleep(2)
