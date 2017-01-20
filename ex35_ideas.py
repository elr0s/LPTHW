from sys import exit

def contain_only(inputString):
	return all(char.isdigit() for char in inputString)

def extract_digits_only(inputString):
	count = ''
	for char in inputString:
		if char.isdigit():
			count += char
	return count

	# count = "".join([c for c in inputString if c.isdigit()])
	# return count

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if  contain_only(next):
		how_much = int(extract_digits_only(next))
	else:
	 	print "Man, learn to type a number."

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		print "You greedy bastard!"

gold_room()
