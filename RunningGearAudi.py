from RunningGear import RunningGear
from SuspensionAudi import SuspensionAudi
from WheelAudi import WheelAudi

class RunningGearAudi(RunningGear):
    def __init__(self):
        RunningGear.__init__(self, SuspensionAudi(), WheelAudi(), WheelAudi(), WheelAudi(), WheelAudi())
