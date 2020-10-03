import random
name = input('Hello, What is your name?')

number = random.randint(1,30)

print(name + ', enter a number between 0 and 30')
tries = 0
win = 0
print('Guess the number within 5 guesses! ')

while tries < 5:
	tries += 1
	print("Try Number:", tries, end=" ")
	try:
        	guess = int(input())
    	except:
        	print("Invalid Input")
        	i = 1
        	break

	if guess < number and tries != 5:
		print('The number is too low, try again')

	if guess > number:	
		print('The number is too high, try again')

	if guess == number:
		print('Well done, you guessed it right')
		win=1
		break

if win == 0 and not i:
	print('You lost,' + name)
