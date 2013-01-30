from Chassis import Chassis
from RunningGearAudi import RunningGearAudi
from TransmissionAudi import TransmissionAudi
from ControlSystemAudi import ControlSystemAudi

class ChassisFord(Chassis):
    def __init__(self):
        Chassis.__init__(self, RunningGearAudi(), TransmissionAudi(), ControlSystemAudi)
