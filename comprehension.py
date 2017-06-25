import random

guessesTaken = 0

print('Hello! What is your name?')  # prints the specified message
myName = input()  # initialize the variable with the input

number = random.randint(1, 20)  # initialize the variable with a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints the specified message, also the myName variable as the second word

while guessesTaken < 6:  # creates a loop which runs until the condition is true
    print('Take a guess.')  # prints the specified message
    guess = input()  # initialize the variable with the input
    guess = int(guess)  # converts the variable to an integer

    guessesTaken += 1  # increases the variable's value by one

    if guess < number:  # evaluates the expression
        print('Your guess is too low.')  # prints the specified message

    if guess > number:  # evaluates the expression
        print('Your guess is too high.')  # prints the specified message

    if guess == number:  # evaluates the expression
        break  # terminates the loop statement and transfers execution to the statement immediately following the loop.

if guess == number:  # evaluates the expression
    guessesTaken = str(guessesTaken)  # converts the variable to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken +
          ' guesses!')  # prints the specified message, with variables in it

if guess != number:  # evaluates the expression
    number = str(number)  # converts the variable to a string
  
    print('Nope. The number I was thinking of was ' + number)  # prints the specified message, with variables at the end of it
