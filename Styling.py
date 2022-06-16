import colorama
import random
from colorama import Style, Back, Fore
colorama.init(autoreset=True)

def style_shell(string):
	color=Fore.BLUE
	print(color + string)
def style_logo(string):
	color=Fore.YELLOW
	print(color + string)
def style_default(string):
	color=Fore.WHITE
	print(color + string)
def style_alert(string):
	color=Fore.RED
	print(color + string)

def style_success(string):
	color=Fore.GREEN
	print(color + string)	
		
def style_rev():
	string="(reverseshell)"
	style_success(string)
	
