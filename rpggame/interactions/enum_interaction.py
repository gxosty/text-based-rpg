from . import Interaction


class EnumInteraction(Interaction):
	def __init__(self, name, enum):
		super().__init__(name)
		self.enum = enum

	def get_enum(self):
		return self.enum

	def interact(self, game):
		pass