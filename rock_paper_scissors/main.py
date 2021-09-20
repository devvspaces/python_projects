import random



def play():
	user = input("What is your choice: 'r' for Rock, 's' for Scissors, 'p' for Paper: ")
	computer = random.choice(['r', 's', 'p'])

	if user == computer:
		return "It's a tie"

	if is_win(user, computer):
		return 'You won!'

	return 'You lost!'

def is_win(player, opponent):
	if (player == 'r' and opponent == 's')\
	or (player == 'p' and opponent == 'r')\
	or (player == 's' and opponent == 'p'):
		return True


if __name__ == '__main__':
	print(play())