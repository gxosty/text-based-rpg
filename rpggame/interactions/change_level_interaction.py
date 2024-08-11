from . import Interaction
from rpggame.levels import Level


class ChangeLevelInteraction(Interaction):
	def __init__(self, level: Level):
		super().__init__("-> " + level.get_name())
		self.level = level

	def interact(self, game):
		game.set_current_level(self.level)
		game.add_event("You went to " + self.level.get_name())

	def matches(self, text):
		return super().matches(text if text.startswith("->") else "-> " + text.lstrip())