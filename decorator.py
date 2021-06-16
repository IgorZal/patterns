
class Traveler():
    
    def __init__(self, distance, name):
        self.distance = distance
        self.name=name

    def walk(self):
        if self.distance>50:
            raise Exception ("distance too much")
        
        print(f"{self.name} by foot:")
        print(f"{self.distance}km traveled, time {self.distance/5} hours")

        
class AutoTreveler():
    
    def __init__(self,distance,tourist,vehicle):
        self.distance=distance
        self.tourist=tourist
        self.vehicle=vehicle
        self.vehicles={'auto':80,'bicycle':15}
    
    def __getattr__(self, item):
        return getattr(self.tourist, item)
    
    def move(self):
        print(f"{self.tourist.name} by {self.vehicle}:")
        print(f"{self.distance} km traveled, time {self.distance/self.vehicles[self.vehicle]} hours")
        



john=Traveler(40,'John')
x=AutoTreveler(100,john,'auto')
x.move()
x.walk()

