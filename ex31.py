print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		print "You see the long dark corridor. What do you want to do?"
		print "1. Go to the corridor."
		print "2. Go back."

		corridor = raw_input("> ")

		if corridor == "1":
			print "You are going through the corridor."
			print "After 10 steps you fail into the pit right on thorns and die. Good job!"
		else:
			print "You returned to the dark room. A strange shadow stands at the center."
			print "1. Ask a question."
			print "2. Going to the door #2."
			print "3. Do't do anything."

			shadow = raw_input("> ")

			if shadow == "1":
				print "You ask a question, but a shadow keeping silence. You ask again. No answer."
				print "You are trying to touch the shadow with your finger."
				print "Flesh from your finger and then from your arm slips out. Good job!"
			elif shadow == "2" or shadow == "3":
				print "Looks like shadow doesn't like you. At the next moment shadow is close to you."
				print "It bends to your face and kisses you. Flesh from your face slips out. Good job!"
			else: 
				print "You don't have any chance." 
				print "Shadow comes to you, touches and you died from a heart failure. Good job!"

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"
