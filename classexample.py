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

class ResidentialBuilding(Building):
    def __init__(self, name="Unknown", address="Mainstreet 123", people=1):
        super().__init__(name, address)
        self._people = people

    def tostring(self):
        text = super().tostring() + " and people " + str(self._people)
        return text

    #==========================================
    #TODO1: add the properties for people to the class
    @property
    def people(self):
        return "* " + self._people + " *"

    @people.setter
    def people(self, people):
        self._people = people
    #==========================================
    pass

class AppartmentBuilding(ResidentialBuilding):
    pass

class Villa(ResidentialBuilding):
    #==========================================
    #TODO2: add init with _has_swimming_pool, call the super init
    def __init__(self, name="Unknown", address="Mainstreet 123", people=1, has_swimming_pool = False):
        super().__init__(name, address, people)
        self._has_swimming_pool = has_swimming_pool
    #==========================================    

    #==========================================
    #TODO3: add properties for has_swimming_pool
    @property
    def has_swimming_pool(self):
        if self._has_swimming_pool:
            text = "* WITH SWIMMING POOL *"
        else:
            text = "* NO SWIMMING POOL *"
        return text

    @has_swimming_pool.setter
    def has_swimming_pool(self, has_swimming_pool):
        self._has_swimming_pool = has_swimming_pool
    #==========================================

    def tostring(self):
        text = super().tostring() + " and "  +(self.has_swimming_pool)
        return text
        
    pass

def main():
    print("Buildings example")
    building1 = Building("Test Building 1")
    building1.name = "Test Building 2"
    print(building1.name)
    print(building1._name)
    residential1 = ResidentialBuilding(name="res1", address="square 123", people=100)
    print(residential1.name)
    print(residential1.address)
    #print(residential1._people)

    print(residential1.tostring())

    #==========================================
    #TODO4: Test your work
    villa1 = Villa(name="Villa Kakelbont", address="Bosweg 4", people=4, has_swimming_pool = False)
    villa2 = Villa()
    print(villa1.tostring())
    #==========================================

main()
