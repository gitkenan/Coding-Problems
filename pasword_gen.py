# we import some modules to use
import random  
import string

# we define lists of numbers, lowercase letters 
# and capital letters, special characters
number_list = range(1, 27)
number_list2 = range(1, 5)
letter_list = [x for x in string.ascii_lowercase] 
caps_list = [x for x in string.ascii_uppercase]
symbol_list = ['#', '!', '@', '%']

# we define dictionaries which associate numbers 
# 1-26 to letters and numbers 1-4 to special characters
num_to_alph = dict(zip(number_list, letter_list)) # dictionary of numbered lowercase letters
num_to_caps = dict(zip(number_list, caps_list)) # dictionary of numbered uppercase letters
num_to_symbols = dict(zip(number_list2, symbol_list)) # dictionary of numbers to symbols 

# asks the user to input has_uppercase, has_lowercase,
# password_length which are the 'conditions'
def prompt_conditions(): 
	global b
	global a
	a = 0
	b = 0

	print """has_uppercase = 
	1. True
	2. False"""

	answer1 = raw_input("> ")
	
	if answer1 == '1':
		has_uppercase = True

	elif answer1 == '2':
		has_uppercase = False

	else:
		print "This is not an option. Try again."
		prompt_conditions()


	print """has_symbols = 
	1. True
	2. False"""

	answer2 = raw_input("> ")

	if answer2 == '1':
		has_symbols = True

	elif answer2 == '2':
		has_symbols = False

	else:
		print "This is not an option. Try again."
		prompt_conditions()

	if has_uppercase == True:
		a = random.randint(1, 3)

	elif has_uppercase == False:
		a = 0

	else:
		pass


	if has_symbols == True:
		b = random.randint(1, 3)
		
	elif has_symbols == False:
		b = 0
		
	else:
		pass


# This function will use our lists, dictionaries and parameters
# a and b to define a password which may or may not contain
# special characters or capital letters depending on the 
# conditions
def random_list(password_length):
	list_of_letters = []

	for k in range(0, a):
		list_of_letters.append(num_to_caps[random.randint(1, 26)])

	for k in range(0, b):
		list_of_letters.append(num_to_symbols[random.randint(1, 4)])

	for k in range(0, password_length - a - b):
		list_of_letters.append(num_to_alph[random.randint(1, 26)])

	password = ''.join(random.sample(list_of_letters, password_length)) # Shuffle the letters

	print password


prompt_conditions()

k = raw_input("""
password_length = """)

random_list(int(k))