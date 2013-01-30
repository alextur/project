from Wheel import Wheel
from Firm import Firm

class WheelFord(Wheel):
    def __init__(self):
        Wheel.__init__(self, Firm.FORD)
