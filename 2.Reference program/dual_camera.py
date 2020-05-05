import sensor
import image
import lcd
import time

lcd.init()

sensor.binocular_reset()
sensor.shutdown(0)  # choose sensor 0
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

sensor.shutdown(1)  # choose sensor 1
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

while True:
    sensor.shutdown(0)  # choose sensor 0
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)

    sensor.shutdown(1)  # choose sensor 1
    img = sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)
