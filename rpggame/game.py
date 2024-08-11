import rpggame
from rpggame import utils

from .player import Player
from .levels import Level
from .states import *
from .interactions import *

from typing import List

import colorama as clr


class Game:
	def __init__(self):
		self._initialize_levels()

		self.player = Player()
		self.is_running = True
		self.current_level = self._get_level("Home")

		self.states = [IdleState()]
		self.messages = []
		self.events = []

	def _print_info(self):
		utils.clear_console()
		print(clr.Fore.LIGHTCYAN_EX + "Write \"!quit\" if you want to quit the game")
		print("------------------------------------------\n" + clr.Fore.LIGHTGREEN_EX)

		print("You are currently at:", self.current_level.get_name())
		print("\nPlayer stats:")
		print("- HP:", self.player.get_health())
		print("- MP:", self.player.get_mana())

		if armour := self.player.get_armour():
			print("- Armour:", armour.get_name())

		if weapon := self.player.get_weapon():
			print("- Weapon:", weapon.get_name())

		if self.events:
			print(clr.Fore.BLACK, clr.Back.WHITE)

			for event in self.events:
				print("> ", event)

			self.events.clear()
			print(clr.Back.RESET, end="")

		if self.messages:
			print(clr.Fore.YELLOW)
			print("New Messages:")

			for message in self.messages:
				print(">>", message)

			self.messages.clear()

		print(clr.Fore.RESET)

	def run(self):
		rpggame._current_game = self

		while self.is_running:
			self._print_info()
			self.get_state().update(self)

		rpggame._current_game = None

	def get_state(self):
		return self.states[-1]

	def push_state(self, state: State):
		self.states.append(state)

	def pop_state(self):
		self.states.pop()

	def set_current_level(self, level: Level):
		self.current_level = level

	def get_current_level(self):
		return self.current_level

	def add_message(self, message: str):
		self.messages.append(message)

	def add_event(self, event: str):
		self.events.append(event)

	def get_player_interaction(self, interactions: List[Interaction]) -> int:
		print("Your next actions:")

		for idx, interaction in enumerate(interactions):
			print(f"[{idx + 1}] {interaction.get_name()}")

		player_input = input("\n> ").strip()

		if not player_input:
			return None

		if player_input.startswith("!quit"):
			exit(0)

		if not player_input.isdigit():
			for interaction in interactions:
				if interaction.matches(player_input):
					return interaction

			return None

		player_input = int(player_input) - 1

		if player_input < 0 or player_input >= len(interactions):
			return None

		return interactions[player_input]

	def _initialize_levels(self):
		from rpggame import levels
		self._levels = {}

		home = levels.Home()
		windhelm = levels.Windhelm()
		greenhollow = levels.Greenhollow()
		stonepeak = levels.Stonepeak()

		home.add_route(windhelm)

		windhelm.add_route(home)
		windhelm.add_route(greenhollow)
		windhelm.add_route(stonepeak)

		greenhollow.add_route(windhelm)

		stonepeak.add_route(windhelm)

		self._register_level(home)
		self._register_level(windhelm)
		self._register_level(greenhollow)
		self._register_level(stonepeak)

	def _register_level(self, level):
		self._levels[level.name] = level

	def _get_level(self, level_name):
		return self._levels[level_name]