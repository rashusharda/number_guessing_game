import random # to import random module

n = random.randrange(1,100) # to create a range of random numbers between 1-100

guess = int(input("Enter any number: ")) # to take a user input to enter a number
print ("\n")

while n!= guess: # means if n is not equal to the input guess
        
        if guess < n: # if guess is smaller than n
            print("Too low")
            guess = int(input("Enter number again: ")) # to again ask for input
            print ("\n")

        elif guess > n: # if guess is greater than n
            print("Too high!") # to again ask for the user input
            guess = int(input("Enter number again: ")) # if guess gets equals to n terminate the while loop
            print ("\n")

        else:
            break # program is stopped

print("You guessed it right!!")
print ("\n")
print("Thank you for playing the number guess game!")
print ("\n")