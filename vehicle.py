#!/usr/bin/env python
 
class Vehicle(object):
    
    def __init__(self):
        self.make = ''
        self.model = ''

    def setModel(self, model):
        self.model = model

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def getMake(self):
        return self.make

class motorVehicle(Vehicle):

    def __init__(self):
        self.engine = ''

    def setEngine(self, engine):
        self.engine = engine

    def getEngine(self):
        return self.engine

class bicycle(Vehicle):

    def __init__(self):
        self.speed = 0
        self.gear = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setGear(self, gear):
        self.gear = gear

    def getSpeed(self):
        return self.speed

    def getGear(self):
        return self.gear

class Car(motorVehicle):

    def __init__(self):
        self.wheels = 0
        self.seat = 0
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setWheels(self, wheels):
        self.wheels = wheels

    def setSeat(self, seat):
        self.seat = seat

    def getSpeed(self):
        return self.speed

    def getWheels(self):
        return self.wheels

    def getSeat(self):
        return self.seat

class Truck(motorVehicle):

    def __init__(self):
        self.wheels = 0
        self.seat = 0
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setWheels(self, wheels):
        self.wheels = wheels

    def setSeat(self, seat):
        self.seat = seat

    def getSpeed(self):
        return self.speed

    def getWheels(self):
        return self.wheels

    def getSeat(self):
        return self.seat

class MotorCycle(motorVehicle):

    def __init__(self):
        self.wheels = 0
        self.seat = 0
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setWheels(self, wheels):
        self.wheels = wheels

    def setSeat(self, seat):
        self.seat = seat

    def getSpeed(self):
        return self.speed

    def getWheels(self):
        return self.wheels

    def getSeat(self):
        return self.seat        
                          
if __name__ == "__main__":
    car = Car()
    car.setModel('Suzuki')
    car.setMake('2014')
    car.setEngine('Petrol')
    car.setSpeed(120)
    car.setWheels(4)
    car.setSeat(5)
    print "Model is %s" % car.getModel()
    print "Make is %s" % car.getMake()
    print "Engine Type is %s" % car.getEngine()
    print "MaxSpeed is %s" % car.getSpeed()
    print "Number of Wheels are %s" % car.getWheels()
    print "Total seating capacity is %s" % car.getSeat()