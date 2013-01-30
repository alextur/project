from Suspension import Suspension
from Firm import Firm

class SuspensionAudi(Suspension):
    def __init__(self):
        Suspension.__init__(self, Suspension.TYPE_INDEPENDENT, Firm.AUDI)
