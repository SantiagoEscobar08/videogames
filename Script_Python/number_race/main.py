
from random import randint
import os

status_game=True

def main_menu():
    print("::: MAIN MENU :::")
    print("[1]. Start Game")
    print("[2]. About us")
    print("[3]. Exit")
    opt = int(input("Press any option: "))
    return opt

while status_game:
    os.system('clear')
    op = main_menu()
    if op == 1:
        print("Game under construction")
        key = input("Press any key to go to the main menu...")
    elif op == 2:
        print("Help under construction")
        key = input("Press any key to go to the main menu...")
    else:
        print("See you later")
        key = input("Press any key to exit...")
        break
        

'''
dice1= randint(1,6)
dice2= randint(1,6)

print(f"Dice 1: {dice1}")
print(f"Dice 2: {dice2}")
'''
