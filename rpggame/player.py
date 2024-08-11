from .entities import Entity


class Player(Entity):
	def __init__(self):
		super().__init__(health=100, mana=100, dodge_chance=0, attack_damage=5)