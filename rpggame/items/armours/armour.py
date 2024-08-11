from rpggame.items import Item, ItemType


class ArmourItem(Item):
	def __init__(self, name: str, defense: float, durability: float):
		super().__init__(self, name, ItemType.ARMOR)
		self.defense = defense
		self.durability = durability

	def get_defense(self):
		return self.defense

	def get_durability(self):
		return self.durability

	def decrease_durability_by_damage_taken(self, damage: float):
		self.durability -= damage * 0.1