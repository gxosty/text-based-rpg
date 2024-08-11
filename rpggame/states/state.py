from abc import abstractmethod

class State:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	@abstractmethod
	def update(self, game):
		...