# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n--------------------------------")
print("Welcome to the Password Generator!")
print("----------------------------------\n")

n_letters = int(input("How many letters would you like in your password?\n"))
print("")
n_symbols = int(input("How many symbols would you like?\n"))
print("")
n_numbers = int(input("How many numbers would you like?\n"))
print("")


# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
# for letter in range(0, n_letters):
#    password += random.choice(letters)
# for symbol in range(0, n_symbols):
#    password += random.choice(symbols)
# for number in range(0, n_numbers):
#    password += random.choice(numbers)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
n_characters = n_letters + n_symbols + n_numbers
for character in range(0, n_characters):
    order = random.randint(0, 2)
    # print(f"{n_characters}:{order} / {n_letters}:{n_symbols}:{n_numbers}")
    if order == 0 and n_letters > 0:
        password += random.choice(letters)
        n_letters -= 1
    elif order == 1 and n_symbols > 0:
        password += random.choice(symbols)
        n_symbols -= 1
    elif order == 2 and n_numbers > 0:
        password += random.choice(numbers)
        n_numbers -= 1
    else:
        if n_letters > 0:
            password += random.choice(letters)
            n_letters -= 1
        elif n_symbols > 0:
            password += random.choice(symbols)
            n_symbols -= 1
        else:
            password += random.choice(numbers)
            n_numbers -= 1


print(f"Here is your password: {password}")
