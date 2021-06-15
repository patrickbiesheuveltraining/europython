from building import Building
from residentialbuilding import ResidentialBuilding
from villa import Villa

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

    villa1 = Villa(name="Villa Kakelbont", address="Bosweg 4", people=4, has_swimming_pool = False)
    print(villa1.tostring())

main()
