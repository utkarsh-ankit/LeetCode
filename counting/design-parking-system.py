class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big, self.medium, self.small = big, medium, small
        self.map ={
            1: self.big,
            2: self.medium,
            3: self.small
        }

    def addCar(self, carType: int) -> bool:
        self.map[carType] -= 1
        if self.map[carType] <0:
            self.map[carType] = 0
            return False
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)