from rpggame.items import Item, ItemType

import random


class WeaponItem(Item):
	def __init__(self, name: str, min_damage: float, max_damage: float, durability: float):
		super().__init__(self, name, ItemType.ARMOR)
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.durability = durability

	def get_damage(self):
		return random.randint(self.min_damage, self.max_damage)

	def get_durability(self):
		return self.durability

	def decrease_durability_by_damage_dealt(self, damage: float):
		self.durability -= damage * 0.02