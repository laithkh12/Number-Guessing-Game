from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



# TODO : Function to check user's guess against actual answer
def checkAnswer(userGuess, actualAnswer, turns):
    """
    Checks answer against guess
    :param userGuess:
    :param actualAnswer:
    :param turns:
    :return:
    the number of turns remaining
    """
    if userGuess > actualAnswer:
        print("Too High.")
        return turns - 1
    elif userGuess < actualAnswer:
        print("Too Low.")
        return turns - 1
    elif userGuess == actualAnswer:
        print("Correct.")

# TODO : Function to set difficulty
def setDifficulty():
    level = input("Choose a difficulty level (easy,hard): ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS



def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100!")
    # TODO : Choosing a random number between 1 and 100
    answer = randint(1, 100)

    turns = setDifficulty()


    # TODO : Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left.")
        # TODO : Let the user guess a number
        guess = int(input("Guess a number between 1 and 100: "))
        # TODO : Track the number of turns and reduce by 1 if they get it wrong
        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")



game()