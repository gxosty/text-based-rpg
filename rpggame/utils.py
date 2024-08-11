import os
import platform


def clear_console():
	"""
	Platform independent console clearing
	"""

	if platform.uname().system == "Windows":
		_ = os.system("cls")
	else:
		_ = os.system("clear")