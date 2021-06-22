class Singleton():
   
    def __new__(cls,name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self,name):
      self.name=name


teachers={'nostradamus':'Michele Noterdame', 'vanga':'Vangelia Dimitrova'}

def func(dic):
  for k,v in dic.items():
    k=Singleton(v)
    print(v,k)


func(teachers)