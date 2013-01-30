class GearBox:
    GEAR_1 = 1
    GEAR_2 = 2
    GEAR_3 = 3
    GEAR_R = 'R'
    GEAR_N = 'N'

    def __init__(self, firm):
        self.firm = firm

    def get_gear(self):
        return self.gear

    def set_gear(self, gear):
        self.gear = gear
