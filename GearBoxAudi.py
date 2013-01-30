from GearBox import GearBox
from Firm import Firm

class GearBoxAudi(GearBox):
    def __init__(self):
        GearBox.__init__(self, Firm.Audi)
