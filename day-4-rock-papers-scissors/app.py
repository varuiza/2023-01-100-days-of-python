import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("\n-------------------------------")
print("Let's play Rock Paper Scissors!")
print("-------------------------------\n")

print("What will you choose?")
user_choice = input("Type \"rock\", \"paper\" or \"scissors\".\n").lower()
print("\nYou chose:\n")
if user_choice == "rock":
    print(rock)
elif user_choice == "paper":
    print(paper)
else:
    print(scissors)

cpu_choice = random.randint(0, 2)
print("\nThe CPU chose:")
if cpu_choice == 0:
    print(rock)
elif cpu_choice == 1:
    print(paper)
else:
    print(scissors)

if (user_choice == "rock" and cpu_choice == 2) or (user_choice == "paper" and cpu_choice == 0) or (user_choice == "scissors" and cpu_choice == 1):
    print("You win!")
elif (user_choice == "rock" and cpu_choice == 0) or (user_choice == "paper" and cpu_choice == 1) or (user_choice == "scissors" and cpu_choice == 2):
    print("It's a draw!")
else:
    print("You lose!")
