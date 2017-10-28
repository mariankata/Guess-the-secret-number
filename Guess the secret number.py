import random
secret = random.randint(1,10)
#print secret
print "\nHi, let\'s play a game :)\n"
while True:
    guess = int(raw_input("Guess the secret number (1-10): "))
    if secret == guess:
        print "\nCongratulations!!! You guessed the secret number :)\n"
        break
    else :
        print "\nSorry... Wrong answer :( \nTry again\n"
