import machine
import utime

pot = machine.ADC(26)
led = machine.PWM(machine.Pin(15))
conversion_factor = 3.3 / (65535)
MAX_VOLTAGE = 3.3
led.freq(1000) #1000 hertz

while True:
    voltage = pot.read_u16() * conversion_factor
    print('Voltage: %.1f' % voltage)
    percentage = (voltage / MAX_VOLTAGE) * 100
    print('Percentage: %.0f' % percentage)
    led.duty_u16(pot.read_u16())
    utime.sleep(.25)
