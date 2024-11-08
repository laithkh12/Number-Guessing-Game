# 🎲 Number Guessing Game 🎲

Welcome to the **Number Guessing Game**! In this fun and interactive game, the computer randomly selects a number between 1 and 100, and it's your job to guess what it is. With a limited number of attempts based on the difficulty level you choose, can you guess the correct number?

## 🌟 Features

- **Random Number Generation**: The computer randomly generates a number between 1 and 100 for you to guess.
- **Difficulty Levels**: Choose between easy (10 attempts) and hard (5 attempts).
- **Feedback on Guesses**: Receive feedback on whether your guess is too high, too low, or correct!

## 🎨 Logo

```plaintext
logo = '''
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/           
'''
```

## ⚙️ How It Works
1. The player is prompted to select a difficulty level, which determines the number of attempts allowed.
2. A random number is generated by the computer.
3. The player makes guesses and receives feedback on each guess.
4. The game continues until the player guesses the number or runs out of attempts.

## 📖 Example Usage
```python
# To start the game, simply call the game function.
game()
```

## 💻 Code Snippet
```python
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def checkAnswer(userGuess, actualAnswer, turns):
    if userGuess > actualAnswer:
        print("Too High.")
        return turns - 1
    elif userGuess < actualAnswer:
        print("Too Low.")
        return turns - 1
    elif userGuess == actualAnswer:
        print("Correct.")

def setDifficulty():
    level = input("Choose a difficulty level (easy, hard): ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100!")
    answer = randint(1, 100)
    turns = setDifficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left.")
        guess = int(input("Guess a number between 1 and 100: "))
        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
```

## 🛠️ Requirements
- Python 3.x

## 🎉 Conclusion
Try your luck and see if you can guess the number within the given attempts. Feel free to enhance the game with more features or improve the existing functionalities. Happy guessing! 🎉
