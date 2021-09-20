import random
import string

from words import words


# Reuseable code for joining letters
def join(letters):
	return ' '.join(letters)


# Function to get a valia word, word with no punctuation marks
def get_valid_word():
	word = random.choice(words)

	for i in string.punctuation:
		if i in word:
			return get_valid_word()

	return word


def play(max_guesses=15):

	# Computer will pick a random valid word
	word = get_valid_word()

	pretty = ['_' for i in word]
	used_letters = []

	while max_guesses > 0:
		# User can guess for word
		letter = input(f'You have {max_guesses} guesses, guess a letter from the word the computer guessed: ')

		if letter not in string.ascii_lowercase:
			print('You guessed and invalid character')

		elif letter:
			max_guesses -= 1

			# Append letters to used letters and keep each letter unique
			used_letters.append(letter)
			used_letters = list(set(used_letters))

			# Check if letter is in word
			val = word.find(letter)
			if val == -1:
				print('Letter not correct!')
			
			else:
				# Check if letter has been selected before
				if pretty[val] != '_':
					print('Letter has been selected before!')
					max_guesses += 1
				else:
					print('You got a new letter!')
					pretty[val] = letter
					print(join(pretty))

		print('\n')
		print(f'You have used letter {join(used_letters)} \n')
	
	# Check if user won or not
	if ''.join(pretty) == word:
		print('You won!')
	else: 
		print('You lost!')
		print(f'Real word is --> {word} and You got this --> {join(pretty)}')


if __name__ == '__main__':
	play()