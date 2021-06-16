from abc import ABC, abstractmethod

class Engine:

	def start_engine(self):
		print('the engine is running!')

	def stop_engine(self):
		print('the engine is stopped!')


class AbstractCommand(ABC):

	@abstractmethod
	def execute(self):
		pass


class EngineturnON(AbstractCommand):

	def __init__(self,engine):
		self.engine=engine

	def execute(self):
		self.engine.start_engine()


class EngineturnOff(AbstractCommand):

	def __init__(self,engine):
		self.engine=engine

	def execute(self):
		self.engine.stop_engine()


class CarInterface:

	def __init__(self, on, off):
		self.on=on
		self.off=off

	def turn_on(self):
		self.on.execute()

	def turn_off(self):
		self.off.execute()


m50=Engine()
st=EngineturnON(m50)
sp=EngineturnOff(m50)
bmw=CarInterface(st,sp)


bmw.turn_on()
bmw.turn_off()