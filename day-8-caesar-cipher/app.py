logo = '''           
\n----------------------------------------------------------------
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88

           88             88                                            
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
----------------------------------------------------------------\n
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_message = True

print(logo)


def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    for letter in input_text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            if cipher_direction == "encode":
                letter_position_shifted = letter_position + shift_amount
                # To prevent "out of bound" errors, we check the shifted position against the number of letters in alphabet
                if letter_position_shifted >= len(alphabet):
                    letter_position_shifted = letter_position_shifted % len(
                        alphabet)
            elif cipher_direction == "decode":
                letter_position_shifted = letter_position - shift_amount
            output_text += alphabet[letter_position_shifted]
        else:
            output_text += letter
    print(f"\nThis is your {cipher_direction}d message:\n{output_text}")


while new_message:

    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    go_again = input(
        "\nType \"yes\" if you want to go again, otherwise type \"no\":\n")
    if go_again == "yes":
        new_message = True
    elif go_again == "no":
        new_message = False

print()
print("Goodbye, Caesar!")
