from GearBox import GearBox
from Firm import Firm

class GearBoxFord(GearBox):
    def __init__(self):
        GearBox.__init__(self, Firm.FORD)
