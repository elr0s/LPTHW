from sys import argv

script, first, second, orange = argv
print "This is first %s." % first
print "This is second %s." % second
print "This is orange %s." % orange

argv = raw_input('Another argument: ')
another = argv
print another