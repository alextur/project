from ControlSystem import ControlSystem
from Rudder import Rudder
from Pedal import Pedal

class ControlSystemFord:
    def __init__(self):
        ControlSystem.__init__(self, Rudder(), Pedal(Pedal.TYPE_GAS), Pedal(Pedal.TYPE_BRAKE))
