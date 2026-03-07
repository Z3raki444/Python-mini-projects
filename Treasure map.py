print('''           |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
      ''')
print("Welcome to the Treasure Map!")
print("Your mission is to find the treasure.")
direction = input("Which direction do you want to go? Type 'left' or 'right': ").lower()
if direction == "left":
    action = input("You come to a lake. Do you want to 'swim' or 'wait' for a boat? ").lower()
    if action == "wait":
        door = input("You arrive at a house with three doors. Do you want to open the 'red', 'blue', or 'yellow' door? ").lower()
        if door == "yellow":
            print("Congratulations! You found the treasure! 🏆")
        elif door == "blue":
            print("You enter a room full of beasts. Game over! 💀")
        elif door == "red":
            print("You found a room full of fire. Game over! 🔥")
        else:
            print("You chose a door that doesn't exist. Game over! 🚪")
    else:
        print("You got attacked by a hungry shark. Game over! 🦈") 
else:
    print("You fell into a hole. Game over! 🕳️" )
# This code implements a simple text-based treasure hunt game.