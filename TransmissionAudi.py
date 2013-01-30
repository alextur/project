from Transmission import Transmission
from GearBoxAudi import GearBoxAudi
from Pedal import Pedal

class TransmissionAudi(Transmission):
    def __init__(self):
        Transmission.__init__(self, GearBoxAudi(), Pedal(Pedal.TYPE_CLUTCH))
