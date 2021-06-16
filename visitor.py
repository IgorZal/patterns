class Visitor:
 
  def km_to_ml(self,eu):
    print(f'{eu.range}km={eu.range*0.6}ml')

  def ml_to_km(self,usa):
    print(f'{usa.range}ml={usa.range/0.6}km')


class BaseOdometr:

  def __init__(self,range):
    self.range=range

  def accept(self,visitor):

    pass


class UsaOdometr(BaseOdometr):

  def accept(self,visitor):
    visitor.ml_to_km(self)


class EuOdometr(BaseOdometr):

  def accept(self,visitor):
    visitor.km_to_ml(self)


usa=UsaOdometr(120)
eu=EuOdometr(80)
v=Visitor()
usa.accept(v)
eu.accept(v)
