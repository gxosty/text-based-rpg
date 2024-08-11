from .game import Game

_current_game: Game = None


def get_current_game():
	return _current_game


def init():
	import platform
	import colorama

	if platform.uname().system == "Windows":
		colorama.init()

init()

del init