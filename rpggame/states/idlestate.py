from . import State
from rpggame.interactions import (
	Interaction,
	ChangeLevelInteraction,
	EnumInteraction,
	EmptyInteraction
)

import enum


class IdleState(State):
	class Menu(enum.StrEnum):
		MAIN = enum.auto()
		GOTO = enum.auto()

	def __init__(self):
		super().__init__("Idle")
		self.menu = IdleState.Menu.MAIN

	def get_main_interactions(self):
		return [
			EmptyInteraction("Explore"),
			EnumInteraction("Go to", IdleState.Menu.GOTO)
		]

	def get_goto_interactions(self, game):
		interactions = [
			EnumInteraction("Back to main", IdleState.Menu.MAIN)
		]

		for level in game.get_current_level().get_routes():
			interactions.append(
				ChangeLevelInteraction(level)
			)

		return interactions

	def get_interactions(self, game):
		match self.menu:
			case IdleState.Menu.MAIN:
				return self.get_main_interactions()

			case IdleState.Menu.GOTO:
				return self.get_goto_interactions(game)

	def update(self, game):
		interaction = game.get_player_interaction(self.get_interactions(game))

		if not interaction:
			game.add_message("Please choose proper action")
			return

		interaction_type = type(interaction)

		if interaction_type is EnumInteraction:
			self.menu = interaction.get_enum()

		elif interaction_type is ChangeLevelInteraction:
			interaction.interact(game)
			self.menu = IdleState.Menu.MAIN