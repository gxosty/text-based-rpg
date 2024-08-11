from abc import abstractmethod


class Level:
	def __init__(self, name):
		self.name = name
		self.routes = []
		self.interactions = []
		self.entities = []

	def get_name(self):
		return self.name

	def add_route(self, level: "Level"):
		self.routes.append(level)

	def get_routes(self):
		return self.routes

	def add_interaction(self, interaction: "LevelInteraction"):
		self.interactions.append(interaction)

	def get_interactions(self):
		return self.interactions

	@abstractmethod
	def interact(self, game, interaction: "LevelInteraction"):
		...