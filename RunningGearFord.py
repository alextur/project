from RunningGear import RunningGear
from SuspensionFord import SuspensionFord
from WheelFord import WheelFord

class RunningGearFord(RunningGear):
    def __init__(self):
        RunningGear.__init__(self, SuspensionFord(), WheelFord(), WheelFord(), WheelFord(), WheelFord())
