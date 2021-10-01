"""
Design a parking system for a parking lot. The parking lot has three kinds of 
parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem 
class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the 
car that wants to get into the parking lot. carType can be of three kinds: big, medium, 
or small, which are represented by 1, 2, and 3 respectively. A car can only park in a 
parking space of its carType. If there is no space available, return false, else park 
the car in that size space and return true.
"""

class ParkingSystem(object):
    
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spots = {1: big, 2: medium, 3: small}
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        self.spots[carType] -= 1
        return self.spots[carType] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)