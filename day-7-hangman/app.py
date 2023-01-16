import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
world_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:

    print()
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess and display[position] == "_":
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, that's not in the word. You lose a life.")

    print()
    print(display)
    print()
    print(hangman_art.stages[lives])
    print(f"Lives: {lives}")

    if "_" not in display:
        end_of_game = True
        print()
        print("You win!")

    if lives == 0:
        end_of_game = True
        print()
        print(f"You lose! The word was {chosen_word}")
