tel = {'jack': 4098, 'kate': 7722}
tel['alex'] = 9322

print tel

print tel.has_key('jack')

print tel.get('jack')

print tel['jack']

for name, phone in tel.items():
	print "%s's phone is %d" % (name, phone)

new = tel.pop('jack', 'smth')

print new