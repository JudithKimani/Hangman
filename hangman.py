import random
from words import words

def get_valid_word(words):
    return random.choice(words).upper() #a randomly chosen word from the word list.

def hangman ():
    word = get_valid_word(words)
    word_letters = set(word)
    guessed_letters = set() #what the user has guessed.
    lives = 6

#getting the user's input
    while len(word_letters)>0 and lives> 0:
        # we have to keep track of the letter used.
        print("You have:", lives, "lives")
        print("You have used these letter:", " ".join(guessed_letters))

        word_list = [letter if letter in guessed_letters else "_" for letter in word]
        print("current words: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter.isalpha() and len(user_letter) == 1:
            if user_letter in guessed_letters:
                print("You have already used this letter. Please try again!")
            else:
                guessed_letters.add(user_letter)
                
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives -1
                    print("the letter is not in the word")

        else:
            print("You have already used this letter. Please try again!") 
    if lives == 0:
            print ("Sorry, you died, the words was", word)
    else:
            print("You guessed right!The words was", word)

if __name__ == "__main__":
   hangman()



