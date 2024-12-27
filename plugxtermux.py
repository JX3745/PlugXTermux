import os
import sys
from colorama import Fore, Style

MENU_COLOR = Fore.YELLOW + Style.BRIGHT
RESET = Style.RESET_ALL

def display_menu():
    print(MENU_COLOR + """
    =======================
       PlugXTermux Toolkit
    =======================
    1. Brute Force Login
    2. Phishing Simulation
    3. Credential Checker
    4. Generate Honeytokens
    5. Account Access
    6. Wire Transfer
    7. Bypass Login
    0. Exit
    =======================
    """ + RESET)

def run_tool(option):
    try:
        if option == "1":
            os.system("python scripts/bruteforce.py")
        elif option == "2":
            os.system("python scripts/phishing_simulator.py")
        elif option == "3":
            os.system("python scripts/credential_checker.py")
        elif option == "4":
            os.system("python scripts/honeytoken_generator.py")
        elif option == "5":
            os.system("python scripts/account_access.py")
        elif option == "6":
            os.system("python scripts/transfer_tool.py")
        elif option == "7":
            os.system("python scripts/bypass_login.py")
        elif option == "0":
            print(Fore.GREEN + "Exiting PlugXTermux. Stay secure!" + RESET)
            sys.exit()
        else:
            print(Fore.RED + "Invalid option. Please try again." + RESET)
    except Exception as e:
        print(Fore.RED + f"Error occurred: {str(e)}" + RESET)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input(MENU_COLOR + "Select an option: " + RESET)
        run_tool(choice)
