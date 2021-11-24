import time
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses
import pico_4wd as car
MOTOR_FORWARD_POWER = 40
import time
def callback(data, addr, ctrl):
    if data == 68:
        timeout = time.time() + 3
        for i in range(0,100):
            car.move('backward',MOTOR_FORWARD_POWER)
            print('goodbye')
        car.move("stop")

        data = 0
    if data == 67:
        timeout = time.time() + 3 
        for i in range(0,10):
            car.move('forward',MOTOR_FORWARD_POWER)
        data = 0
        print('hello')       
    print(data)
    

ir = NEC_8(Pin(19, Pin.IN), callback)