from random import choice

def start_madlib():
	# Set the default values
	adjectives = ['beautiful', 'amazing', 'smelly', 'erotic']
	nouns = ['tunde', 'segun', 'car', 'plane']
	verbs = ['running', 'jump', 'dancing', 'swim']

	if input('Use default values (n(No) or *(Yes): ') == 'n':
		adjectives = [input('Enter an Adjective: ') for i in range(3)]
		nouns = [input('Enter a Noun: ') for i in range(3)]
		verbs = [input('Enter a Verb: ') for i in range(3)]

	words = {
		'a': adjectives,
		'n': nouns,
		'v': verbs
	}

	def random_word(type):
		try:
			return choice(words[type])
		except KeyError:
			return


	text = f'''I am a {random_word('a')} person among the other players. \
But {random_word('n')} said i am a {random_word('a')} player, maybe because i {random_word('v')} {random_word('a')}. \
The thing is i love her because she is {random_word('a')}'''

	return text


if __name__ == "__main__":
	print(start_madlib())