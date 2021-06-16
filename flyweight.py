

class Body:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class BodyFactory:
   
    bodies={}

    @classmethod
    def get_type(cls, name):
        value = cls.bodies.get(name)
        if value is None:
            value=Body(name)
            cls.bodies[name]=value
            return value
        else:
        	return value


class CarBody():

    def __init__(self, vinnumber, type_body):
        self.vinnumber=vinnumber
       
        self.type=BodyFactory.get_type(type_body)

    def __str__(self):
        return f'vin number:{self.vinnumber} color:{self.type}'


bmw= CarBody(1234, 'Sedan') 
merc=CarBody(5678, 'Universal') 
audi=CarBody(9101, 'Sedan')

print(bmw)
print(merc)  
print(audi)
print(bmw.type==audi.type)