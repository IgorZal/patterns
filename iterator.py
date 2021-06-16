
class Flow:
  def __init__(self,collection):
    self.collection=collection

  def __iter__(self):
    return ReverseIterator(self, self.collection)
  
  def get(self, index):
    return self.collection[index]
  

class ReverseIterator:
  def __init__(self, obj, collect):
    self.obj=obj
    self.collect=collect
    self.cursor=len(collect)-1
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.cursor>=0:
      pos = self.cursor
      self.cursor-=1
      return self.obj.get(pos)
    else:
      raise StopIteration()


x= Flow([7,8,9,10,11,12])  
for number in list(x):
  print(number)

