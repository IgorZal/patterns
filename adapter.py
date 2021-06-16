class AmericanCar:
    
    def __init__(self,odometr):
        self.odometr=odometr

    def show_distance(self):
        print(self.odometr.show_miles())

        
class Odometr():
    
    def __init__(self,value):
        self.value=value

        
class GermanCarOdometr(Odometr):
    
    def show_kilometers(self):
        return self.value

    
class AmericanCarOdometr(Odometr):
    
    def show_miles(self):
        return self.value

    
class Adapter():
    def __init__(self,value):
        self.german=GermanCarOdometr(value)

    def show_miles(self):
        x=self.german.show_kilometers()
        return x/1.6


bmw=Adapter(100)
usa=AmericanCar(bmw)
usa.show_distance()
