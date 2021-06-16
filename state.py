from abc import ABC, abstractmethod

class BaseState:

	@abstractmethod
	def launch(self):
		pass

	@abstractmethod
	def detonation(self):
		pass


class InFlight(BaseState):
	
	def launch(self):
		return 'Error: the rocket is already launched!'

	def detonation(self):
		return 'Boom!'


class ReadyForLaunch(BaseState):

	def launch(self):
		return 'rocket launch was successful!'

	def detonation(self):
		return 'Error: too low a height!'


class Rocket:

	def __init__(self):
		self.curstate=None

	def set_state(self,state):
		self.curstate=state
		print(f'{self.curstate} activated')

	def launch(self):
		print(self.curstate.launch())

	def detonation(self):
		print(self.curstate.detonation())


n=ReadyForLaunch()
b=InFlight
voevoda=Rocket()
voevoda.set_state(n)
voevoda.launch()

