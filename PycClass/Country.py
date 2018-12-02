#!/usr/bin/python3

class Country:
    def __init__(self,name,gdp,ctype):
        self.name = name
        self.gdp = gdp
        self.ctype = ctype

    def introduction(self):
        print("the country of %s ,gdp is %s ,we are %s"%(self.name,self.gdp,self.ctype))

c = Country("china","9","develop")
c.introduction()
