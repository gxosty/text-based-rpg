from . import Interaction


class EmptyInteraction(Interaction):
	def __init__(self, name):
		super().__init__(name)

	def interact(self, game):
		return