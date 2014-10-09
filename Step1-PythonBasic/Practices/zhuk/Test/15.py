from sys import argv

script, filename = argv

print argv[0]
print argv[1]

txt = open(filename)

print "here's your file %r:" % filename

print txt.read()

print "type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()