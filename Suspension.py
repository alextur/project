class Suspension:
    TYPE_INDEPENDENT = 'independent'
    TYPE_DEPENDENT   = 'dependent'

    def __init__(self, type, firm):
        self.type = type
        self.firm = firm
