from abc import abstractmethod


class Interaction:
	def __init__(self, name):
		self.name = name

	@abstractmethod
	def interact(self, game):
		...

	def matches(self, text: str) -> bool:
		return self.name.lower() == text.lower()

	def get_name(self):
		return self.name