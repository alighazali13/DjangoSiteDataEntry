from pyfiglet import Figlet
from colorama import Fore
import os,  platform

def banner_up():
    platform_os = platform.system()

    if platform_os == "Windows":
    #clear terminal
        os.system("cls")
    else:
        os.system("clear")

    banner = Figlet()

    print(Fore.RED + banner.renderText('XiiiOnTheCode') )
    print(Fore.RED + "> Admin BOT ------------v.1 <")
    print(Fore.WHITE) 
