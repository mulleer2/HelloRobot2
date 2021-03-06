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

    def zig_zag(self):
        """drives forward turns, then goes forward then turns back"""
        fwd()
        time.sleep(.2)
        left()
        time.sleep(.2)
        fwd()
        time.sleep(.2)
        right()
        time.sleep(.4)
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)







p = Piggy()


def menu():
    while True:
        input = raw_input("Press 1 for cruise \n Press 2 for pulse \n Press 3 for sweep \n Press 4 for Zig Zag")
        if "1" in input:
            p.cruise()
        elif "2" in input:
            p.pulse()
        elif "3" in input:
            p.servo_sweep()
        elif "4" in input:
            p.zig_zag()
        else:
            print("Sorry Im not that talented.")


try:
    menu()
except(KeyboardInterrupt, SystemExit):
    from gopigo import *
    stop()







