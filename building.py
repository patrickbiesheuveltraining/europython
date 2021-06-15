class Building:
    def __init__(self, name="Unknown", address="Mainstreet 123"):
        self._name = name
        self._address = address

    @property
    def name(self):
        return "* " + self._name + " *"

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return "* " + self._address + " *"

    @address.setter
    def address(self, address):
        self._address = address

    def tostring(self):
        return "Building with name: "+self.name+" and address "+ self.address
    pass
