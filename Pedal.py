class Pedal:
    STATUS_ON  = 'on'
    STATUS_OFF = 'off'

    TYPE_CLUTCH = 'clutch'
    TYPE_BRAKE  = 'brake'
    TYPE_GAS    = 'gas'

    def __init__(self, type):
        self.type    = type
        self._status = self.STATUS_OFF

    def on(self):
        self._status = self.STATUS_ON

    def off(self):
        self._status = self.STATUS_OFF
