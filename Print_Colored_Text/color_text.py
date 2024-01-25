import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(
    Fore.BLUE
    + Back.YELLOW
    + "Hi My name is Tanay Dwivedi."
    + Fore.YELLOW
    + Back.BLUE
    + "I am learning Data Science."
)
print(Back.CYAN + "Hi My name is Tanay Dwivedi.")
print(Fore.RED + Back.GREEN + "Hi My name is Tanay Dwivedi.")
