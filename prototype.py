from abc import ABC, abstractmethod
import copy

class GeoObject(ABC):

  @abstractmethod
  def clone(self):
    pass

  @abstractmethod
  def set_param():
    pass

    
class Mountain(GeoObject):

  def clone(self):
    return copy.deepcopy(self)
  
  def set_param(self,n,h):
    self.name=n
    self.hight=h

  def __str__(self):
    print(self.name+':'+self.hight)
      

class River(GeoObject):

  def clone(self):
    return copy.deepcopy(self)
  
  def set_param(self,n,l):
    self.name=n
    self.lenght=l

  def __str__(self):
    return self.name+':'+self.lenght  


class Discoverer:
  def __init__(self):
    self.types = [Mountain(), River()]
  
  def make(self, index):
    return self.types[index].clone()     


d=Discoverer()
p=d.make(1)
p.set_param('Monblan','4700m')
print(p)
