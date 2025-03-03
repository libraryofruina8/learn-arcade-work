import random

def instructions_one():
    print("Welcome to Camel!")

def instructions_two():
    print("You have stolen a camel to make your way across the great Mobi desert.")

def instructions_three():
    print("The natives want their camel back and are chasing you down!")

def instructions_four():
    print("Survive your desert trek and out run the natives.")

def main():
    instructions_one()
    instructions_two()
    instructions_three()
    instructions_four()

main()

camel_miles_traveled = 0
camel_thirst = 0
camel_tiredness = 0
natives_distance = -20
initial_canteen = 3

done = False

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status (check.")
    print("Q. Quit.")

    choice = input("\nWhat's your choice? ")
    choice = choice.lower()

    if choice == "Q" or "q":
        done = True
        print("You have chosen to quit!")

    elif choice == "E" or "e":
        print("Miles traveled: ", camel_miles_traveled)
        print("Drinks in canteen: ", initial_canteen)
        print("The natives are ", natives_distance, " miles behind you.")

    elif choice == "D" or "d":
        camel_tiredness = 0
        print("The camel is happy!")
        natives_distance = natives_distance + random.randrange(7, 15)

    elif choice == "C" or "c":
        print("camel_miles_traveled + 15")
