from Transmission import Transmission
from GearBoxFord import GearBoxFord
from Pedal import Pedal

class TransmissionFord(Transmission):
    def __init__(self):
        Transmission.__init__(self, GearBoxFord(), Pedal(Pedal.TYPE_CLUTCH))
