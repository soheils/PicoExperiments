import time
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses
import pico_4wd as car
MOTOR_FORWARD_POWER = 40

def callback(data, addr, ctrl):
    if data == 68:
        car.move('backward',MOTOR_FORWARD_POWER)
        print('hello')
    if data == 67:
        
    print(data)
    

ir = NEC_8(Pin(19, Pin.IN), callback)
while True:
    time.sleep_ms(500)