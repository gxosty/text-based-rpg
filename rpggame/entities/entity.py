import rpggame

import random
import enum


class EntityState(enum.IntEnum):
	"""
	Enum to represent the state of an entity (Dead or Alive).
	"""
	DEAD = enum.auto()
	ALIVE = enum.auto()


class Entity:
	"""
	Base class representing a game entity with health and combat capabilities.

	This class defines common properties and methods for entities in a game. 
	Specific entity types (like Player or Enemy) will inherit from this class 
	and implement the abstract methods.
	"""

	def __init__(self, health: float, mana: float, armour: "rpggame.items.armours.ArmourItem" = None,
				weapon: "rpggame.items.weapons.WeaponItem" = None, dodge_chance: float = 0.0,
				attack_damage: float = 0):
		"""
		Initializes an Entity object.

		Args:
			health: (float) The starting health of the entity.
			armour: (rpggame.items.armours.ArmourItem, default None) The armour value reducing incoming damage.
			dodge_chance: (float, 0.0 to 1.0, default 0) The chance of the entity dodging an attack.
			attack_damage: (float, default 0) The attack damage of the entity
		"""
		self.max_health = health
		self.health = health
		self.mana = mana
		self.armour = armour
		self.weapon = weapon
		self.dodge_chance = dodge_chance
		self.attack_damage = attack_damage
		self.state = EntityState.ALIVE  # Initial state is alive

	def get_health(self):
		return self.health

	def get_mana(self):
		return self.mana

	def get_dodge_chance(self):
		return self.dodge_chance

	def get_attack_damage(self):
		return self.attack_damage

	def get_armour(self):
		return self.armour

	def get_weapon(self):
		return self.weapon

	def take_damage(self, damage: float) -> bool:
		"""
		Simulates taking damage, considering armour and dodge chance.

		Args:
			damage: (float) The amount of damage received.

		Returns:
			True if the damage was applied, False if dodged.
		"""
		if random.uniform() < self.get_dodge_chance():  # Check for dodge
			return False

		armour = self.get_armour()

		if armour:
			# Reduce damage by half `armour.defense` value, minimum 0.25
			damage = max(damage - armour.get_defense() / 2, 0.25)

		self.health -= damage

		if self.health <= 0:
			self.health = 0
			self.state = EntityState.DEAD

		return True  # Damage applied

	def attack(self, entity: "Entity") -> tuple[bool, False]:
		damage = self.attack_damage
		weapon = self.get_weapon()

		if self.weapon:
			damage += weapon.get_damage()

		damage_taken = entity.take_damage(damage)

		if damage_taken:
			weapon.decrease_durability_by_damage_dealt(damage)

		return damage_taken, damage


	def is_alive(self) -> bool:
		"""
		Checks if the entity is alive based on its state.

		Returns:
			True if the entity's state is EntityState.ALIVE, False otherwise.
		"""
		return self.state is EntityState.ALIVE

	def add_health(self, health: float):
		"""
		Adds health points to the entity health

		Args:
			health: (float) the amount of health healed
		"""
		self.health = min(self.health + health, self.max_health)