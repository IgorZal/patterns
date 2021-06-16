import copy

class Prototype:
    def __init__(self):
        self.objects={}
        self.current_obj=None

    def add_obj(self, name, obj):
        self.objects[name] = obj
        
    def del_obj(self, name):
        del self.objects[name]

    def set_current_obj(self,key):
        self.current_obj=key
    
    def clone(self, name, attrs):
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(attrs)
        return obj

class Mountain():
    pass

class River():
    pass

prototype=Prototype()
prototype.add_obj('rock', Mountain())
m1=prototype.clone('rock',{'name':'Monblan','hight':'4800'})
prototype.add_obj('water', River())
r1=prototype.clone('water',{'name':'Volga','lenght':'3500'})






