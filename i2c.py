import machine
import utime
from esp8266_i2c_lcd import I2cLcd

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
lcd=I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()
lcd.putstr("Hello\nWorld")
utime.sleep(5)
lcd.clear()
lcd.backlight_off()
