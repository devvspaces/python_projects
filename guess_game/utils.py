from random import randint

def guess(min = 1, max = 3):
	return randint(min, max)

def user_game(default=5):

	# Get a limit value from the user, this value is going to be the limit of
	# the guessing, if not provided the default will be used as limit
	limit = input(f'Enter the limit for the guess (default is {default}): ')
	limit = int(limit) if limit else default

	# Computer should guess a number here
	comp_guess = guess(max=limit)
	user_guess = 0

	# Run the loop until user guess is right, then show number of guesses made
	count = 0
	while user_guess != comp_guess:
		user_guess = int(input(f'Enter what the computer guessed between 1 to {limit}: '))

		if user_guess > comp_guess:
			print('Sorry, guess again, too high')
		elif user_guess < comp_guess:
			print('Sorry, guess again, too low')
		
		count += 1

	return f'You got it right after {count} guesses'


def comp_game():

	"""
	Computer will randomly select a limit, user will guess a value and computer
	will try to get that value
	"""

	# random limit
	limit = guess(min=5, max=1000)
	minimum = 1

	# User should guess a number here
	user_guess = int(input(f'Pick a number between 1 to {limit}: '))

	# Validate user picks
	if user_guess < 1 or user_guess > limit:
		raise ValueError

	comp_guess = 0

	# Run the loop until user guess is right, then show number of guesses made
	count = 0
	while comp_guess != user_guess:
		comp_guess = guess(min=minimum, max=limit)

		# Block of code below makes computer make faster guesses
		if comp_guess > user_guess:
			limit = comp_guess
		elif comp_guess < user_guess:
			minimum = comp_guess
		# ======================================================

		count += 1

	return f'Computer got it right after {count} guesses'