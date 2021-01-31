import machine
import utime

pot = machine.ADC(26)
conversion_factor = 3.3 / (65535)
MAX_VOLTAGE = 3.3

while True:
    voltage = pot.read_u16() * conversion_factor
    print('Voltage: %.1f' % voltage)
    percentage = (voltage / MAX_VOLTAGE) * 100
    print('Percentage: %.0f' % percentage)
    utime.sleep(2)
