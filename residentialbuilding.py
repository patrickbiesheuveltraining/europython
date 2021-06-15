from building import Building

class ResidentialBuilding(Building):
    def __init__(self, name="Unknown", address="Mainstreet 123", people=1):
        super().__init__(name, address)
        self._people = people

    def tostring(self):
        text = super().tostring() + " and people " + str(self._people)
        return text

    #TODO1: add the properties for people to the class
    @property
    def people(self):
        return "* " + self._people + " *"

    @people.setter
    def people(self, people):
        self._people = people
    
    pass
