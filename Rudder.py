class Rudder:
    STATUS_LEFT      = 'left'
    STATUS_RIGHT     = 'right'
    STATUS_NEUTRALLY = 'neutrally'

    def __init__(self):
        self._status = self.STATUS_NEUTRALLY

    def left(self):
        self._status = self.STATUS_LEFT

    def right(self):
        self._status = self.STATUS_RIGHT

    def neutrally(self):
        self._status = self.STATUS_NEUTRALLY
