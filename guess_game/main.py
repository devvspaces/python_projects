from utils import user_game, comp_game


def play(func):

	try:
		print(func())

	except ValueError:
		# If there was a value error, the function will be called again
		print('\n Try Again')
		return play(func)

	except KeyboardInterrupt:
		# When ctrl + c is used, end the game, instead of showing errors
		print('Game Over')


if __name__ == '__main__':
	player = input('Who is guessing: 1 for You and 2 for Computer: ')

	if player == '1':
		play(user_game)
	elif player == '2':
		play(comp_game)
	else:
		print('Please enter a right value')