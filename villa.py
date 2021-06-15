from residentialbuilding import ResidentialBuilding

class Villa(ResidentialBuilding):
    # add init with _has_swimming_pool, call the super init
    def __init__(self, name="Unknown", address="Mainstreet 123", people=1, has_swimming_pool = False):
        super().__init__(name, address, people)
        self._has_swimming_pool = has_swimming_pool
        
    #add properties for has_swimming_pool
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

    def tostring(self):
        text = super().tostring() + " and "  +(self.has_swimming_pool)
        return text
        
    pass
