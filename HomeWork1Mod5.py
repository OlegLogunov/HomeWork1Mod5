class House:

    def __init__(self):
        self.numberOfFloors = 10

myhouse = House()

while myhouse.numberOfFloors > 0:
    print("Текущий этаж равен", myhouse.numberOfFloors)
    myhouse.numberOfFloors -=1
