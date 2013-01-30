from Body import Body
from Firm import Firm
from Material import Material

class BodyFord(Body):
    def __init__(self):
        Body.__init__(self, Firm.FORD, Material.STEEL)
