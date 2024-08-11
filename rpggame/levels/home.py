from . import Level

class Home(Level):
	def __init__(self):
		super().__init__("Home")

	def interact(self, game, interaction):
		pass