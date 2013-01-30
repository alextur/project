from Wheel import Wheel
from Firm import Firm

class WheelAudi(Wheel):
    def __init__(self):
        Wheel.__init__(self, Firm.AUDI)
