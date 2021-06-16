from abc import ABC, abstractmethod
import random

class Uber(ABC):

	def __init__(self, distance):
		self.distance=distance

	def order_taxi(self):
		self.show_arrival_time()
		self.show_travel_time()
		self.show_price()

	@abstractmethod
	def show_price(self):
		pass

	def show_arrival_time(self):
		print(f'arrival time: {random.randint(1,15)} minutes')

	def show_travel_time(self):
		print(f'travel time: {self.distance/40*60} minutes')


class Econom(Uber):

	def show_price(self):
		print(f'pay: {self.distance*10} UAH')
		

class Bussines(Uber):

	def show_price(self):
		print(f'pay: {self.distance*20} UAH')


sam=Bussines(8)
sam.order_taxi()

		
	
