class Teacher():
    '''Only one teacher at the classrom'''
    def __new__(cls,name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Teacher, cls).__new__(cls)
        return cls.instance

    def __init__(self,name):
      self.name=name


teachers={'nostradamus':'Michele Noterdame', 'vanga':'Vangelia Dimitrova'}

def func(dic):
  for k,v in dic.items():
    k=Teacher(v)
    print(v,k)


func(teachers)