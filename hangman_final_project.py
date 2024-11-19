import random
print("HELLO ! YOU HAVE TO GUESS THE RIGHT NAME OF ONE OF YOUR CLASSMATE. ALL THE BEST !")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
# TODO-1: - Update the name  list to use the 'name_list' from hangman_words.py
name_list=['abhishek','abhiroop','aditya','ansh','mohit','manish','pushpank','shivesh','ranjana','shweta','divyata','shikha','khushi','apoorva','anshika','aradhya','atul','naved','priyanshu']
chosen_name=random.choice(name_list)
#print(chosen_name)

# TODO-2: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_length = len(chosen_name)
for position in range(word_length):
    placeholder += "_"
#print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-3: Update the code below to tell the user how many lives they have left.
    print(f"YOU HAVE {lives} LIVES LEFT")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for letter in chosen_name:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)
    print("YOUR GUESS IS RUGHT.NOW GOUESS THE NEXT LETTER")

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_name:
        lives -= 1
        print(" OUPS! WRONG GUESS! YOU LOSE 1 LIFE.")
        print(stages[lives])
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print("IT WAS WRONG GUESS!YOU LOSE!")


    if "_" not in display:
        game_over = True
        print("YOU GUESS THE RIGHT NAME , CONGRATULATIONS! YOU WIN!!")

    #print(stages[lives])
