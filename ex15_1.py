print "Type the filename: "
filename = raw_input('> ')

file = open(filename)

print "Here is your file %r." % filename
print file.read()
file.close()

file = open(filename)
print "----"
print file.name
print file.mode
line = file.readlines()
print line
line = file.readlines()
print line
file.close()

file = open(filename)
line = file.readline()
print line
line = file.readline(14)
print line
file.close()