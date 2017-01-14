from sys import argv

script, filename = argv

print "We'r going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate() # not nessesary because of 'w' mode in line 12

print "Now, I'am going to ask for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
lines = line1 + "\n" + line2 + "\n" + line3 + "\n"

print "I'm going to write these to the file."

target.write(lines)

print "And finally, we close it."
target.close()