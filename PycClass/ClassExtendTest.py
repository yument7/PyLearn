#!/usr/bin/python3
# --coding=utf-8--

class Device:
    def __init__(self,partno,categoryName):
        self.partno = partno
        self.categoryName = categoryName
    
    def using(self):
        pass

# ---------------------------单继承：Resitor Capacitor-------------------------  
class Resistor(Device):
    def __init__(self,partno,categoryName,resistance,voltage):
        Device.__init__(self,partno,categoryName)
        self.resistance = resistance
        self.voltage = voltage
    
    def using(self):
        print("i am resistor")

class Capacitor(Device):
    def __init__(self,partno,categoryName,capacity,power):
        Device.__init__(self,partno,categoryName)
        self.capacity = capacity
        self.power = power
    
    def using(self):
        print("i am capacitor")

# ---------------------------多继承：Mainbord-----------------------------------------
class Mainbord(Resistor,Capacitor):
    def __init__(self,size,boradtype):
        self.size = size
        self.boradtype = boradtype

    def using(self):
        print("i am mainbord , i extend resistor and capacitor")



if __name__ == '__main__':
    resistor = Resistor('123','电阻','50','1.0')
    capacitor = Capacitor('124','电容','12','0.03')
    resistor.using()
    capacitor.using()
    