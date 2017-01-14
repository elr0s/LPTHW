def magic_animals(kittens, unicorns):
	print "We have %d kittens sitting on the floor!" % kittens
	print "We have %d unicorns playing on the grass!" % unicorns
	print "Omg! Isn't it amazing?!\n"

magic_animals(17, 28)

fluffy_kittens = 14
brave_unicorns = 21

magic_animals(fluffy_kittens, brave_unicorns)

magic_animals(117 + 27, 2 + 228)

magic_animals(fluffy_kittens - 1, brave_unicorns + 7)

user_desire = int(raw_input('How many kittens do you want to sit on the floor? '))
user_dream = int(raw_input('How many unicorns do you want to see playing on the grass? '))

magic_animals(user_desire, user_dream)

magic_animals(int(raw_input('Just testing! ')), 17)