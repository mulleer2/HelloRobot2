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

p = Piggy()
p.dab()


