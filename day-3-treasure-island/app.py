print('''
*******************************************************************************
          |                   |                  |                     |
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Can you find the treasure?\n")

# Write your code below this line 👇
print("You're at a crossroad. Where do you want to go?")
crossroad = (input("Type \"left\" or \"right\".\n")).lower()
if crossroad == "left":
    print("\nYou've come to a lake. There is an island in the middle of the lake. Will you wait for a boat or swim across?")
    lake = input("Type \"wait\" or \"swim\".\n").lower()
    if lake == "wait":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour will you choose?")
        door = input("Type \"red\", \"yellow\" or \"blue\".\n").lower()
        if door == "red":
            print("\nYou open the red door and enter to the room. Suddenly, the door closes and you find youself surrounded by fire. Game over!")
        elif door == "yellow":
            print("\nYou open the yellow door and enter to the room. Inside, you find some chest filled with coins and gems. You win!")
        elif door == "blue":
            print("\nYou open the blue door and enter to the room. Inside, you are attacked with a lot of wild beasts. Game over!")
        else:
            print("\nA black hole opens before you and engulf everything. Game over!")
    else:
        print("\nThe lake monster ate you. Game over!")
else:
    print("\nYou fell into a hole. Game over!")
