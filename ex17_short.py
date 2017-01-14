# One way to write this script
# from sys import argv

# script, from_file, to_file = argv

# in_file = open(from_file)
# indata = in_file.read()

# outfile = open(to_file, 'w')
# outfile.write(indata)

# in_file.close()
# outfile.close()


# Another way to write this script
# from sys import argv; script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read()
# outfile = open(to_file, 'w'); outfile.write(indata); in_file.close(); outfile.close()


# Third way to write this script
from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()
outdata = open(to_file, 'w').write(indata)
