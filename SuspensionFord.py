from Suspension import Suspension
from Firm import Firm

class SuspensionFord(Suspension):
    def __init__(self):
        Suspension.__init__(self, Suspension.TYPE_INDEPENDENT, Firm.FORD)
