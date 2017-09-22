from gopigo import *

import time

class Piggy(object):

    def __init__(self):
        print("I am alive")

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()

    def dab(self):
        for x in range(5):
            fwd()
            time.sleep(.5)
            bwd()
            time.sleep(.5)
            right_rot()
            time.sleep(.5)
            stop()



    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15)  # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()



    def cruise(self):
        """drive forward, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)







    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(30, 160, 2):
            servo(ang)
            time.sleep(.2)




p = Piggy()


message = input("What would you like to do? pulse or cruise or sweep").lower()

if message == "pulse":
    p.pulse()
elif message == "cruise":
    p.cruise()
elif message == "sweep":
    p.servo_sweep()
else:
    print("Sorry, I can't do that")








