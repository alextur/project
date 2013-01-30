from Chassis import Chassis
from RunningGearFord import RunningGearFord
from TransmissionFord import TransmissionFord
from ControlSystemFord import ControlSystemFord

class ChassisFord(Chassis):
    def __init__(self):
        Chassis.__init__(self, RunningGearFord(), TransmissionFord(), ControlSystemFord)
