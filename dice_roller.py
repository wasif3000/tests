from random import random, randint, uniform

def roll_dice():
    print("Select a dice to roll from D4 to D100: ")
    dice_choice = int(input("Enter Dice Type (e.g., 4, 6, 8, 10, 12, 20, 100): "))
    dice_amount = int(input("Enter number of dice to roll: "))
    modifiers = int(input("Enter any modifiers to the dice total: "))

    total_roll = 0
    for _ in range(dice_amount):
        roll = randint (1, dice_choice)
        total_roll += roll

    total_with_modifiers = total_roll + modifiers

    print(f"You rolled a total of {total_roll} from the dice.")
    print(f"After adding modifiers, your final total is {total_with_modifiers}.")

roll_dice()