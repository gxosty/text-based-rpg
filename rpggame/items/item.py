import enum


class ItemType(enum.StrEnum):
	ITEM = "Item"
	WEAPON = "Weapon"
	ARMOR = "Armor"
	POTION = "Potion"
	FOOD = "Food"


class Item:
	def __init__(self, name: str, item_type: ItemType = ItemType.ITEM):
		self.name = name
		self.item_type = item_type

	def get_type(self):
		return self.item_type